import sys
sys.setrecursionlimit(100000000)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
N = int(input())
G = [[] for _ in range(N)]
edge = []
for i in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b,i,1))
    G[b].append((a,i,-1))
    edge.append((a,b))
ans = [-1]*N
ans[0] = 0
rank = [-1]*N
rank[0] = 0
q = [0]
while q:
    i = q.pop()
    for ni,e,k in G[i]:
        if rank[ni] >= 0:
            continue
        rank[ni] = rank[i] + 1
        q.append(ni)
# def dfs(i,vi,r):
#     rank[i] = r
#     for ni,e,k in G[i]:
#         if ni == vi:
#             continue
#         dfs(ni,i,r+1)
# dfs(0,0,0)
Q = int(input())
C = [0]*(N-1)
for _ in range(Q):
    t,e,x = map(int,input().split())
    e -= 1
    a,b = edge[e]
    if t == 1:
        if rank[a] < rank[b]:
            ans[0] += x
        C[e] -= x
    else:
        if rank[a] > rank[b]:
            ans[0] += x
        C[e] += x
q = [0]
while q:
    i = q.pop()
    for ni,e,k in G[i]:
        if ans[ni] == -1:
            ans[ni] = ans[i] + C[e]*k
            q.append(ni)
# def dfs1(i,vi):
#     for ni,e,k in G[i]:
#         if ni == vi:
#             continue
#         ans[ni] = ans[i] + C[e]*k
#         dfs1(ni,i)
# dfs1(0,0)
for a in ans:
    print(a)