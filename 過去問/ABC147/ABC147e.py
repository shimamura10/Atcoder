H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]
c = 6400
dp = [[0 for _ in range(W)]for _ in range(H)]
D = []
for i in range(H):
    tmp = []
    for j in range(W):
        tmp.append(abs(A[i][j]-B[i][j]))
    D.append(tmp)
dp[0][0] |= 1<<(c+D[0][0])
dp[0][0] |= 1<<(c-D[0][0])
# dp[0][0][-D[0][0]%81] = 1
for i in range(H):
    for j in range(W):
        if i > 0:
            dp[i][j] |= dp[i-1][j] << D[i][j]
            dp[i][j] |= dp[i-1][j] >> D[i][j]
        if j > 0:
            dp[i][j] |= dp[i][j-1] << D[i][j]
            dp[i][j] |= dp[i][j-1] >> D[i][j]
for a in range(81):
    if ((dp[-1][-1] >> (c+a)) & 1) or ((dp[-1][-1] >> (c-a)) & 1):
        ans = a
        break
print(ans)