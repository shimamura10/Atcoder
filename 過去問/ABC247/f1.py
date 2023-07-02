N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
G = [-1]*N
for i in range(N):
    p = P[i] - 1
    q = Q[i] - 1
    G[p] = q
    # G[q].append(p)
seen = [False]*N
def dfs(i):
    seen[i] = True
    ret = 1
    for ni in G[i]:
        if seen[ni]:
            continue
        ret += dfs(ni)
    return ret
cnt = []
for i in range(N):
    if seen[i]:
        continue
    # cnt.append(dfs(i))
    seen[i] = True
    tmp = 1
    ni = G[i]
    while ni != i:
        seen[ni] = True
        ni = G[ni]
        tmp += 1
    cnt.append(tmp)
mod = 998244353
f = [2,3]
for i in range(2,N):
    f.append((f[i-2]+f[i-1])%mod)
g = [1,3,4]
for i in range(3,N):
    g.append((f[i-1]+f[i-3])%mod)
ans = 1
for c in cnt:
    ans = ans*g[c-1]%mod
print(ans)