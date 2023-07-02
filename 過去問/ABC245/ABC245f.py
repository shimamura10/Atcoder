import sys
sys.setrecursionlimit(100000000)
N,M = map(int,input().split())
G = [[] for _ in range(N)]
G_rev = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G_rev[b].append(a)
stack = []
seen = [False]*N
seen2 = [False]*N
def dfs(v):
    if seen[v]:
        stack.append(v)
        seen[v] = False
        return
    if seen2[v]:
        return
    seen[v] = True
    seen2[v] = True
    for i in G[v]:
        dfs(i)
    seen[v] = False
seen1 = [False]*N
def dfs1(v):
    seen1[v] = True
    for i in G_rev[v]:
        if seen1[i]:
            continue
        dfs1(i)
for i in range(N):
    if seen2[i]:
        continue
    dfs(i)
for i in stack:
    if seen1[i]:
        continue
    dfs1(i)
ans = 0
for i in range(N):
    if seen1[i]:
        ans += 1
print(ans)



