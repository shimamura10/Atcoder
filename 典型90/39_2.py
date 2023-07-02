import sys
sys.setrecursionlimit(100000000)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
V = [0]*N
def dfs(i,vi):
    res = 1
    for ni in G[i]:
        if ni == vi:
            continue
        res += dfs(ni,i)
    V[i] = res
    return res
dfs(0,0)
ans = 0
def dfs1(i,vi):
    global ans
    ans += (N-V[i])*V[i]
    for ni in G[i]:
        if ni == vi:
            continue
        dfs1(ni,i)
dfs1(0,0)
print(ans)