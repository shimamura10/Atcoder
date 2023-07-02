N = int(input())
mod = 10**9+7
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

ans = []
for k in range(1,N+1):
    tmp = 0
    for a in range(1,(N-1)//k+2):
        tmp += cmb(N-(k-1)*(a-1),a)
        tmp %= mod
    ans.append(tmp)
for a in ans:
    print(a)