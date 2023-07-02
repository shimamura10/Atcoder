N,M,Q = map(int,input().split())
G = []
import sys
sys.setrecursionlimit(100000000)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
for _ in range(Q):
    a,b,c,d = map(int,input().split())
    # a -= 1
    # b -= 1
    G.append((a,b,c,d))
A = []
ans = 0
def dfs(i,n):
    A.append(i)
    if n == N:
        ret = 0
        for a,b,c,d in G:
            if A[b] - A[a] == c:
                ret += d
        global ans
        ans = max(ans,ret)
        del A[-1]
        return
    for ni in range(i,M):
        dfs(ni,n+1)
    del A[-1]
dfs(0,0)
print(ans)