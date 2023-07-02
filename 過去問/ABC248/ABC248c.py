N,M,K = map(int,input().split())
mod = 998244353
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for a in range(1,M+1):
        for j in range(K-a+1):
            dp[i+1][j+a] += dp[i][j]
            dp[i+1][j+a] %= mod
ans = 0
for i in range(K+1):
    ans += dp[-1][i]
print(ans%mod)