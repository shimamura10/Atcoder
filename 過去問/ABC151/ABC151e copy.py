import enum
from itertools import accumulate


N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 10**9 + 7
MAX = N # MAX は必要分だけ用意する
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

def cmb(n, r, p=mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

for i in range(2, MAX + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)
ans = 0
A.sort()
for i,a in enumerate(A):
    ans += a*cmb(i,K-1)
    ans -= a*cmb(N-i-1,K-1)
    ans %= mod
print(ans)