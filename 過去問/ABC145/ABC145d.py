X,Y = map(int,input().split())
mod = 10**9 + 7
MAX = X+Y # MAX は必要分だけ用意する
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
if (2*X-Y)%3 == 0 and (2*Y-X)%3 == 0 and (2*X-Y)//3 >= 0 and (2*Y-X)//3 >= 0:
    a = (2*X-Y)//3
    b = (2*Y-X)//3
    print(cmb(a+b,b))
else:
    print(0)