N = int(input())
X,Y = map(int,input().split())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
inf = float('inf')
dp = [[[inf]*(Y+1) for _ in range(X+1)] for _ in range(N+1)]
for i in range(N):
    dp[i][0][0] = 0
for i in range(N):
    for j in range(X+1):
        for k in range(Y+1):
            dp[i+1][j][k] = min(dp[i][j][k],dp[i][max(0,j-A[i])][max(0,k-B[i])]+1)
if dp[N][X][Y] == inf:
    print(-1)
else:
    print(dp[N][X][Y])