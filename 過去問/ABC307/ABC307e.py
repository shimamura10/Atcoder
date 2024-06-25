N,M = map(int,input().split())
same = M
notSame = 0
mod = 998244353
for i in range(N-1):
  tmpsame = same
  same = notSame
  notSame = tmpsame*(M-1) + notSame*(M-2)
  same %= mod
  notSame %= mod
print(notSame%mod)