class BIT():  #要素番号は始めを1としていることに注意
    def __init__(self,n,mod=0):
        self.BIT = [0]*(n+1)
        self.num = n
        self.mod = mod

    def query(self,idx):  #1からidx番目までの和を返す
        res_sum = 0
        mod = self.mod
        while idx > 0:
            res_sum += self.BIT[idx]
            if mod:
                res_sum %= mod
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):  #idx番目の要素にxを足す
        mod = self.mod
        while idx <= self.num:
            self.BIT[idx] += x
            if mod:
                self.BIT[idx] %= mod
            idx += idx&(-idx)
        return
from bisect import bisect_left, bisect_right
from collections import defaultdict


N,M,Q = map(int,input().split())
que = []
ans = []
lad = []
x = [-1]*(N+1)
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 3:
        ans.append([N*q[2]+q[1],i])
        lad.append(N*q[2]+q[1])
    que.append(q)
ans.sort()
lad.sort()
pos = defaultdict(int)
for i,a in enumerate(ans):
    pos[a[1]] = i
for i,q in enumerate(que):
    if q[0] == 2:
        x[q[1]] = i
    if q[0] == 3:
        if x[q[1]] >= 0:
            que[x[q[1]]].append(pos[i])

bit = BIT(len(ans))
A = [0]*len(ans)
for n,q in enumerate(que):
    if q[0] == 1:
        l = bisect_right(lad,N*q[1])
        r = bisect_right(lad,N*(q[2]+1),0)
        if l < len(ans):
            bit.update(l+1,q[3])
        if r < len(ans):
            bit.update(r+1,-q[3])
    if q[0] == 2:
        x = q[2]
        for i in q[3:]:
            A[i] = -bit.query(i+1) + x
    if q[0] == 3:
        print(A[pos[n]] + bit.query(pos[n]+1))
