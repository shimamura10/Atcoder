N = int(input())
C = list(input().split())
G = [[] for _ in range(N)]
mod = 10**9 + 7
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
def dfs(v,pv):
    if C[v] == 'a':
        a = True
        b = False
    else:
        a = False
        b = True
    tmp = []
    for i in G[v]:
        if i == pv:
            continue
        tmp.append(dfs(i,v))
    res = 1
    re = 1
    for n,na,nb in tmp:
        if C[v] == 'a':
            if nb:
                re *= n
                b = True
        if C[v] == 'b':
            if na:
                re *= n
                a = True
        if na and nb:
            res *= 2*n%mod
    res -= re
    if not a or not b:
        res = 0
    return [res%mod,a,b]
print(dfs(0,0)[0])