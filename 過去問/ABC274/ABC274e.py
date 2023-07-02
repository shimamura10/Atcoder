from math import factorial, sqrt


N, M = map(int,input().split())
inf = float('inf')
dp = [[inf]*(1<<(N+M+1)) for _ in range(N+M+1)]
boost = [1]*(1<<(N+M+1))
dis = [[inf]*(N+M+1) for _ in range(N+M+1)]
xy = [[0,0]] + [list(map(int,input().split())) for _ in range(N+M)]
for i in range(N+M+1):
    for j in range(N+M+1):
        dis[i][j] = sqrt((xy[i][0]-xy[j][0])**2 + (xy[i][1]-xy[j][1])**2)
for s in range(1<<(N+M+1)):
    cnt = 0
    for i in range(M):
        if 1 <<(i+N+1) & s:
            cnt += 1
    boost[s] = 2**cnt
dp[0][1] = 0
for s in range(1<<(N+M+1)):
    for i in range(N+M+1):
        if 1 << i & s:
            t = s - (1 << i)
            for j in range(N+M+1):
                if 1 << j & t and i != j:
                    dp[i][s] = min(dp[i][s],dp[j][t] + dis[j][i]/boost[t])
ans = inf
for s in range(1<<(N+M+1)):
    ok = True
    for i in range(N+1):
        if not (1 << i & s):
            ok = False
            break
    if ok == False:
        continue
    for i in range(1,N+M+1):
        ans = min(ans,dp[i][s] + dis[i][0]/boost[s])
print(ans)

# print(factorial(17)//factorial(12)//factorial(5))