N,u,v = map(int,input().split())
u -= 1
v -= 1
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
D = []
def dfs(i,vi):
    res = False
    for ni in G[i]:
        if ni == vi:
            continue
        if dfs(ni,i):
            D.append(ni)
            res = True
    if i == v:
        res = True
    return res
dfs(u,u)
M = 0
def dfs1(i,vi,n):
    global M
    for ni in G[i]:
        if ni == vi or ni == D[-1]:
            continue
        M = max(M,dfs1(ni,i,n+1))
    return n
dfs1(u,u,0)
print(M+len(D)-1)