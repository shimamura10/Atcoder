import sys
sys.setrecursionlimit(100000000)
N,M,K,S,T,X = map(int,input().split())
S -= 1
T -= 1
X -= 1
mod = 998244353
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dp = [[[-1,-1] for _ in range(K+1)] for _ in range(N)]
def dfs(v,j,cnt):
    if v == X:
        cnt = 1 - cnt
    # if dp[v][j][cnt] != -1:
    #     return dp[v][j][cnt]
    if j == K:
        if cnt != 0:
            dp[v][j][cnt] = 0
            return 0
        if v == T:
            dp[v][j][cnt] = 1
            return 1
        else:
            dp[v][j][cnt] = 0
            return 0
    res = 0
    for i in G[v]:
        if i == X:
            if dp[i][j+1][1-cnt] != -1:
                res += dp[i][j+1][1-cnt]
                continue
        elif dp[i][j+1][cnt] != -1:
            res += dp[i][j+1][cnt]
            continue
        res += dfs(i,j+1,cnt)
    dp[v][j][cnt] = res%mod
    return res%mod
print(dfs(S,0,0))
# print(dp)
