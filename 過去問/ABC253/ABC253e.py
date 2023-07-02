N,M,K = map(int,input().split())
mod = 998244353
dp = [[0]*M for _ in range(N)]
dp[0] = [1 for _ in range(M)]
if K == 0:
    print(pow(M,N,mod))
    exit()
for i in range(1,N):
    su = sum(dp[i-1])
    su %= mod
    s = sum(dp[i-1][:K-1])
    s %= mod
    for j in range(M):
        if j + K - 1< M:
            s += dp[i-1][j+K-1]
        if j - K >= 0:
            s -= dp[i-1][j-K]
        s %= mod
        dp[i][j] = su - s
        dp[i][j] %= mod
print(sum(dp[-1])%mod)