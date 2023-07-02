N,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
MAX = max(A)+K+1 # MAX は必要分だけ用意する
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
# ans = 1
s = set(A)
app = [-1]*(max(A)+K+1)
app[0] = 0
for i in range(1,len(app)):
    if i-1 in s:
        app[i] = app[i-1]
    else:
        app[i] = app[i-1] + 1
ans = 0
for a,n in enumerate(app):
    if n < K:
        ans += cmb(a+K-n-1,a)
        ans %= mod
print(ans)