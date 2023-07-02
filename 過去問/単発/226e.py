N,M = map(int,input().split())
G = [[] for _ in range(N)]
mod = 998244353
import sys
sys.setrecursionlimit(100000000)
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
seen = [False]*N
def dfs(v):
    seen[v] = True
    global n,m
    n += 1
    m += len(G[v])
    for i in G[v]:
        if not seen[i]:
            dfs(i)

ans = 1
b = True
for i in range(N):
    n = 0
    m = 0
    if not seen[i]:
        dfs(i) 
        if n == m//2:
            ans = ans*2%mod
        else:
            b = False
            break
if b:
    print(ans)
else:
    print(0)