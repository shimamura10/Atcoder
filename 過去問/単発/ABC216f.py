N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = max(max(A),max(B))
mod = 998244353
ab = [(A[i],B[i]) for i in range(N)]
ab.sort()
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(M):
        dp[i+1][j] += dp[i][j]
        if j - ab[i][1] >= 0:
            dp[i+1][j] += dp[i][j-ab[i][1]]
        dp[i+1][j] %= mod
ans = 0
for i in range(N):
    for j in range(ab[i][0]+1-ab[i][1]):
        ans += dp[i][j]
    ans %= mod
print(ans)