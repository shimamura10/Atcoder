N,W = map(int,input().split())
dp = [[0]*(W+1) for _ in range(N+1)]
for i in range(N):
    w,v = map(int,input().split())
    for j in range(W+1):
        if j-w >= 0:
            dp[i+1][j] = max(dp[i][j],v+dp[i][j-w])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[-1][-1])