H,W,C = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
inf = float('inf')
dp1 = [[inf]*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        dp1[i][j] = min(A[i-1][j-1],dp1[i-1][j]+C,dp1[i][j-1]+C)
X1 = [[inf]*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        X1[i][j] = A[i-1][j-1] + min(dp1[i-1][j]+C,dp1[i][j-1]+C)
dp2 = [[inf]*(W+1) for _ in range(H+1)]
for i in reversed(range(H)):
    for j in range(1,W+1):
        dp2[i][j] = min(A[i][j-1],dp2[i+1][j]+C,dp2[i][j-1]+C)
X2 = [[inf]*(W+1) for _ in range(H+1)]
for i in reversed(range(H)):
    for j in range(1,W+1):
        X2[i][j] = A[i][j-1] + min(dp2[i+1][j]+C,dp2[i][j-1]+C)
ans = inf
for i in range(H+1):
    for j in range(W+1):
        ans = min(ans,X1[i][j],X2[i][j])
print(ans)