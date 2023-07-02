K = int(input())
if K%9 == 0:
    mod = 10**9 + 7
    dp = [0]*(K+1)
    for i in range(1,10):
        dp[i] = 1
    for i in range(K+1):
        for j in range(1,min(10,i+1)):
            dp[i] = (dp[i] + dp[i-j])%mod
    print(dp[-1])
else:
    print(0)