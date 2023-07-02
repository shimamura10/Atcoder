N = int(input())
a = list(map(int,input().split()))
mod = 998244353
dp = [[0]*10 for _ in range(N)]
dp[0][a[0]] = 1
for i in range(1,N):
    for j in range(10):
        for k in range(10):
            if (a[i]+k)%10 == j:
                dp[i][j] += dp[i-1][k]%mod
            if (a[i]*k)%10 == j:
                dp[i][j] += dp[i-1][k]%mod
for i in range(10):
    print(dp[-1][i]%mod)
# print(dp)