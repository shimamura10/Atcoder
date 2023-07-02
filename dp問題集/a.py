N = int(input())
p = list(map(int,input().split()))
dp = [[False]*(100*N+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = True
for i in range(N):
    for j in range(1,100*N+1):
        if j - p[i] >= 0:
            dp[i+1][j] = dp[i][j-p[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]
ans = 0
for i in range(100*N+1):
    if dp[N][i]:
        ans += 1
# print(dp[N][:11])
print(ans)
