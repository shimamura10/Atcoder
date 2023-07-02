
S = int(input())
mod = 10**9+7
import sys
sys.setrecursionlimit(100000)

nCr = {}
def cmb(n, r):
    if r == 0 or r == n or n == 0: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]%mod


n = S//3 + 1
ans = 0
for i in range(1,n):
    s = S - 3*i
    ans += cmb(s+i-1,i-1)

print(ans%mod)