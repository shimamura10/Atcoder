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
dp = [[[0,0] for _ in range(N)] for _ in range(K+1)]
dp[0][S][0] = 1
for i in range(K):
    for j in range(N):
        for x in range(2):
            if j == X:
                for v in G[j]:
                    dp[i+1][j][1-x] += dp[i][v][x]%mod
            else:
                for v in G[j]: 
                    dp[i+1][j][x] += dp[i][v][x]%mod
print(dp[K][T][0]%mod)

