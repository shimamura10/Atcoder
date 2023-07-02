N,P = map(int,input().split())
import sys
sys.setrecursionlimit(100000000)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
def cmb(n, r, p=P):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p
 
Ncmb = 2*N # Ncmb は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, Ncmb + 1):
    fact.append((fact[-1] * i) % P)
    inv.append((-inv[P % i] * (P // i)) % P)
    factinv.append((factinv[-1] * inv[-1]) % P)
G = [[] for _ in range(2*N)]
for i in range(N-1):
    G[i].append(i+1)
    G[i+1].append(i)
    G[N+i].append(N+i+1)
    G[N+i+1].append(N+i)
    G[i].append(N+i)
    G[N+i].append(i)
G[N-1].append(2*N-1)
G[2*N-1].append(N-1)
seen = [0]*2*N
def dfs(x,n,k):
    if n == 2*N:
        return 1
    if seen[x] == 0:
        k += 1
    seen[x] += 1
    ret = 0
    for to in G[x]:
        if seen[to]:
            continue
        ret += dfs(to,n+1,k)
    seen[x] = False
    return ret%P
a = dfs(0,1)
ans = [a]
for i in range(N-1):
    ans.append(a*(cmb(2*N-i-i,i+1)))
print(*ans[::-1])



    