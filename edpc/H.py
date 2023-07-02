H,W = map(int,input().split())
a = [input() for _ in range(H)]
dp = [[0]*W for _ in range(H)]
dp[0][0] = 1
mod = 10**9 + 7
for i in range(H):
    for j in range(W):
        if a[i][j] == '#':
            continue
        if i > 0:
            dp[i][j] = (dp[i][j]+dp[i-1][j])%mod
        if j > 0:
            dp[i][j] = (dp[i][j]+dp[i][j-1])%mod
print(dp[-1][-1])