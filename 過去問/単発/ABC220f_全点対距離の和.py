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
n = [0]*N
d = [0]*N
def dfs(v,pv,i):
    d[v] = i
    res = 1
    for j in G[v]:
        if j == pv:
            continue
        res += dfs(j,v,i+1)
    n[v] = res
    return res
dfs(0,0,0)
# print(d,n)
D = sum(d)
ans = [0]*N
ans[0] = D
def dfs1(v,pv,d):
    # print(v)
    global ans
    if v != pv:
        nd = d + N - 2*n[v]
        ans[v] = nd
        # print(nd,v)
    else:
        nd = d
    for i in G[v]:
        if i == pv:
            continue
        dfs1(i,v,nd)
dfs1(0,0,D)
for i in ans:
    print(i)

