N,L = map(int,input().split())
dp = [0]*(N+1)
dp[0] = 1
mod = 10**9 + 7
for i in range(1,N+1):
    if i >= L:
        dp[i] = (dp[i-1] + dp[i-L])%mod
    else:
        dp[i] = dp[i-1]%mod
print(dp[-1])