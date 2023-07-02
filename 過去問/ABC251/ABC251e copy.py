N = int(input())
A = list(map(int,input().split()))
inf = 10**10
dp1 = [[0]*2 for _ in range(N)]
dp1[0][1] = A[0]
dp1[0][0] = inf
for i in range(1,N):
    dp1[i][0] = dp1[i-1][1]
    dp1[i][1] = min(dp1[i-1][0],dp1[i-1][1]) + A[i]
dp2 = [[0]*2 for _ in range(N)]
dp2[0][1] = inf
dp2[0][0] = 0
for i in range(1,N):
    dp2[i][0] = dp2[i-1][1]
    dp2[i][1] = min(dp2[i-1][0],dp2[i-1][1]) + A[i]
ans = dp2[-1][1]
ans = min(ans,dp1[-1][0])
ans = min(ans,dp1[-1][1])
print(ans)