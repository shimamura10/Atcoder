class RollingHash():
    def __init__(self, s, base=37, mod=10**9+9):
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
    def get(self, l, r): #s[l:r]のハッシュ値を取得
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod

N = int(input())
T = input()
hT = T[:N]
eT_rev = T[N:][::-1]
hT_RH = RollingHash(hT)
eT_rev_RH = RollingHash(eT_rev)
for i in range(N):
    if (hT_RH.get(0,i) == eT_rev_RH.get(N-i, N)) and (hT_RH.get(i,N) == (eT_rev_RH.get(0,N-i))):
        print(T[:i] + T[i+N:])
        print(i)
        exit()
print(-1)
