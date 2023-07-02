
N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9 + 7
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1
for i in range(N):
    for j in range(K):
        if j - A[i] < 0:
            dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1])%mod
        else:
            dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1] - dp[i][j - A[i]])%mod
print(dp[-1][-1])

