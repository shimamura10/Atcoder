from collections import defaultdict


def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 3, 5, 7, 11, 13, 17]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = (y * y) % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1
def findFactorRho(n):
    from math import gcd
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n // g): return n // g
            return findFactorRho(g)

def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i*i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += 1 + i % 2
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1: ret[n] = 1
    if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
    return ret
class ModInt:
    def __init__(self, x):
        self.x = x % mod

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, mod - 2, mod)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, mod - 2, mod))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, mod)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, mod))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, mod - 2, mod)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, mod - 2, mod))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, mod)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, mod))
        )
cnt = defaultdict(int)
mod = 10**9+7
N = int(input())
A = list(map(int,input().split()))
for a in A:
    tmp = primeFactor(a)
    for key in tmp.keys():
        cnt[key] = max(cnt[key],tmp[key])
AB = ModInt(1)
for key in cnt.keys():
    AB *= pow(key,cnt[key],mod)
ans = 0
for a in A:
    ans += AB/a
print(ans)
