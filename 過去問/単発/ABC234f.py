from collections import defaultdict


S = input()
freq = defaultdict(int)
for s in S:
    freq[s] += 1
mod = 998244353
MAX = len(S) # MAX は必要分だけ用意する
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

dp = [[0]*(MAX+1) for _ in range(len(freq.keys())+1)]
dp[0][0] = 1
sm = 0
for i,n in enumerate(freq.values()):
    sm += n
    for j in range(sm+1):
        for k in range(min(n,j)+1):
            dp[i+1][j] += dp[i][j-k] * cmb(j,k)
            dp[i+1][j] %= mod
ans = sum(dp[-1]) - 1
ans %= mod
print(ans)