N = int(input())
p = list(map(float,input().split()))
dp = [[0]*(N+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    dp[i+1][0] = (1-p[i])*dp[i][0]
for i in range(N):
    for j in range(N):
        dp[i+1][j+1] = p[i]*dp[i][j] + (1-p[i])*dp[i][j+1]
ans = 0
for i in range(N//2+1,N+1):
    ans += dp[-1][i]
print(ans)