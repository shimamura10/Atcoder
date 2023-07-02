N,M,K = map(int,input().split())
mod = 998244353
P = [1]
for i in range(N):
    P.append(P[i]*(M-1)%mod)
def cmb(n, r, p=mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p
 
 # N は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

ans = 0
for k in range(K+1):
    ans += M%mod*P[N-1-k]*cmb(N-1,k)%mod
    ans %= mod
print(ans)