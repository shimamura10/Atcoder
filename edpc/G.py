import sys
sys.setrecursionlimit(100000000)
N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
dp = [-1]*N
def dfs(pos):
    if dp[pos] != -1:
        return dp[pos]
    res = 0
    for npos in G[pos]:
        res = max(res,dfs(npos)+1)
    dp[pos] = res
    return res
for i in range(N):
    if dp[i] == -1:
        dfs(i)
print(max(dp))
