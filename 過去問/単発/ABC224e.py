N,M,K = map(int,input().split())
mod = 998244353
G = [[i] for i in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dp = [[0]*(N) for _ in range(K+1)]
dp[0][0] = 1
for i in range(K):
    s = sum(dp[i])
    # for k in range(N):
    #     sum = sum + dp[k][j]
    for j in range(N):
        dp[i+1][j] = s
        for v in G[j]:
            dp[i+1][j] -= dp[i][v]
        dp[i+1][j] %= mod
print(dp[-1][0])