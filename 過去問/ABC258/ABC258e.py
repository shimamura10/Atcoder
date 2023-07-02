from bisect import bisect_left
from itertools import accumulate


N,Q,X = map(int,input().split())
W = list(map(int,input().split()))
S = sum(W)
base = X//S*N
X %= S
ans = []
seen = [-1]*N
# seen[0] = 0
acc = list(accumulate([0]+W*2))
end = 0
cnt = 0
n = 0
s = 0
while True:
    if seen[end] != -1:
        n = cnt - seen[end]
        s = seen[end]
        break
    seen[end] = cnt
    cnt += 1
    nex = bisect_left(acc,acc[end]+X)
    w = nex - end
    if nex >= N:
        nex -= N
        # x = X - acc[-1] + acc[end]
        # x %= acc[-1]
        # w += (x//acc[-1])*N
        # nex = bisect_left(acc,x)
        # w += nex
    ans.append(w)
    end = nex
for i in range(Q):
    k = int(input())
    k -= 1
    if k < s:
        print(ans[k]+base)
    else:
        print(ans[s+(k-s)%n]+base)