# ローリングハッシュでは、文字列A(m文字)から、
# 互いに素な基数bとmodの除数hを用いて以下の式でハッシュ値を求めます。

# hash(A) = ( A_0*b^(m-1) + A_1*b^(m-2) + ... + A_(m-1)*b^0 ) mod h

# hが十分に大きいとき文字列ごとのハッシュ値はほとんどユニークなので、
# 文字列s,tのハッシュ値が一致したとき、高確率でs=tである
# といえます。

class RollingHash():
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod
    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod
RH = RollingHash("abcdef", 37, 10**9+9)

S = "abcdef"
print(S[0:5:-1])