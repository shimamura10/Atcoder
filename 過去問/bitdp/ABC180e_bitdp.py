N = int(input())
inf = float('inf')
dp = [[inf]*(1<<N) for _ in range(N)]
dis = [[inf]*N for _ in range(N)]
xyz = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        dis[i][j] = abs(xyz[j][0]-xyz[i][0]) + abs(xyz[j][1]-xyz[i][1]) + max(0,xyz[j][2]-xyz[i][2])
dp[0][1] = 0
for s in range(1<<N):
    for i in range(N):
        if 1 << i & s:
            t = s - (1 << i)
            for j in range(N):
                if 1 << j & t and i != j:
                    dp[i][s] = min(dp[i][s],dp[j][t] + dis[j][i])
ans = inf
for i in range(1,N):
    ans = min(ans,dp[i][-1] + dis[i][0])
print(ans)

