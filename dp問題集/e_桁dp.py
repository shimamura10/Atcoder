
D = int(input())
N = input()
MOD = 10**9+7
dp = [[[0 for _ in range(D)] for _ in range(2)] for _ in range(len(N)+1)]
# n = int(N[0])
# for i in range(n):
#     dp[0][1][i] += 1
# dp[0][0][n%D] += 1
dp[0][0][0] = 1
for i in range(len(N)):
    n = int(N[i])
    for j in range(10):
        for k in range(D):
            dp[i+1][1][(j+k)%D] += dp[i][1][k] % MOD
    for j in range(n):
        for k in range(D):
            dp[i+1][1][(j+k)%D] += dp[i][0][k] % MOD
    for k in range(D):
        dp[i+1][0][(n+k)%D] += dp[i][0][k] % MOD
print((dp[-1][0][0] + dp[-1][1][0] - 1)%MOD)


