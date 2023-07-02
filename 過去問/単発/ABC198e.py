from collections import defaultdict
import sys
sys.setrecursionlimit(100000000)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())
C = list(map(int,input().split()))
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
seen = defaultdict(int)
ans = []
def dfs(v,pv):
    if seen[C[v]] == 0:
        ans.append(v)
    seen[C[v]] += 1
    for nv in G[v]:
        if nv == pv:
            continue
        dfs(nv,v)
    seen[C[v]] -= 1
dfs(0,0)
ans.sort()
for a in ans:
    print(a+1)
