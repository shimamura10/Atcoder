N = int(input())
a = list(map(int,input().split()))
n = []
from bisect import bisect_left
inf = float('inf')
dp = [inf]*len(a)
for i in range(len(a)):
    idx = bisect_left(dp,a[i])
    dp[idx] = a[i]
    n.append(idx+1)
n_rev = []
a_rev = a[::-1]
dp_rev = [inf]*len(a)
for i in range(len(a)):
    idx = bisect_left(dp_rev,a_rev[i])
    dp_rev[idx] = a_rev[i]
    n_rev.append(idx+1)
ans = 0
for i in range(N):
    ans = max(ans,n[i]+n_rev[N-i-1]-1)
print(ans)