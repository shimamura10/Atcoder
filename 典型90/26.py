import sys
sys.setrecursionlimit(100000000)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
A = []
B = []
def dfs(v,pv,add):
    if add:
        A.append(v+1)
    else:
        B.append(v+1)
    for nv in G[v]:
        if nv == pv:
            continue
        dfs(nv,v,not add)
dfs(0,0,0)
if len(A) >= N//2:
    print(*A[:N//2])
else:
    print(*B[:N//2])