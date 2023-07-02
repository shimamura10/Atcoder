N,W  =map(int,input().split())
inf = 10**10
dp = [[inf]*(100001) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0
for i in range(N):
    w,v = map(int,input().split())
    for j in range(100001):
        if j - v >= 0:
            if w + dp[i][j-v] <= W:
                dp[i+1][j] = min(dp[i][j],w + dp[i][j-v])
            else:
                dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]
# print(dp[-2][:18])
for j in range(len(dp[-1])-1,-1,-1):
    if dp[-1][j] < inf:
        print(j)
        exit()
