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
def dfs(v,pv):
    max = 0
    max2 = 0
    for i in G[v]:
        if i == pv:
            continue
        tmp = dfs(i,v)
        if tmp > max:
            max2 = max
            max = tmp
        elif tmp > max2:
            max2 = tmp
    ans[v] = max + max2 + 1
    return max + 1
ans = [0]*N
dfs(0,0)
print(max(ans))