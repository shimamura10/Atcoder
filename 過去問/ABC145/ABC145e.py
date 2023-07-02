N,T = map(int,input().split())
dp = [[0]*(T+1) for _ in range(N+1)]
A = [list(map(int,input().split())) for _ in range(N)]
A.sort()
for i in range(N):
    a,b = A[i]
    for j in range(T):
        if j >= a:
            dp[i+1][j] = max(dp[i][j],dp[i][j-a]+b)
        else:
            dp[i+1][j] = dp[i][j]
    dp[i+1][T] = max(dp[i][T-1] + b,dp[i][T])
print(dp[-1][-1])