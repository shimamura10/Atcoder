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
N,P = map(int,input().split())
mod = 998244353
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

Plist = [1]
Plistbar = [1]
hundred = [1]
for i in range(N+1):
    Plist.append(Plist[-1]*P%mod)
    Plistbar.append(Plistbar[-1]*(100-P)%mod)
    hundred.append(hundred[-1]*100%mod)
ans100N = 0
for i in range(N//2+2):
    ans100N += (N-i)*cmb(N-i,i)%mod*Plist[i]%mod*Plistbar[N-2*i]%mod*hundred[i]%mod
ans = ans100N/ModInt(hundred[N])
if N%2:
    # ans100N += (N//2+1)*Plist[N//2+1]%mod*hundred[N-N//2-1]
    N -= 1
    ans100N = 0
    for i in range(N//2):
        ans100N += (N-i)*cmb(N-i,i)%mod*Plist[i]%mod*Plistbar[N-2*i]%mod*hundred[i]%mod
    tmpans = ans100N/ModInt(hundred[N])
    ans += tmpans + P/ModInt(100)
print(ans)
# print(3*90**3+4000*90+20000)