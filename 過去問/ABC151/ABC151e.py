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
acc = [0]*N
for i in range(N):
    if i < K-2:
        # acc.append(0)
        continue
    # acc.append((acc[-1]+cmb(i,K-2))%mod)
    acc[i] = cmb(i,K-2)
# acc = list(accumulate(acc))
for i in range(N-1):
    acc[i+1] += acc[i]
    acc[i+1] %= mod
ans = 0
A.sort()
if K == 1:
    print(0)
    exit()
if K == 2:
    res = 0
    for i in range(N):
        ans += i*A[i] - res
        res += A[i]
        ans %= mod
        res %= mod
    print(ans)
    exit()
for i,a in enumerate(A):
    ans += a*acc[max(0,i-1)]
    ans -= a*acc[max(0,N-i-2)]
    ans %= mod
print(ans)
