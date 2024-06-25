from collections import defaultdict


N,M = map(int,input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int,input().split()))
Ddict = defaultdict(int)
for i,d in enumerate(D):
  Ddict[d] = P[i+1]
ans = 0
for c in C:
  if c in Ddict:
    ans += Ddict[c]
  else:
    ans += P[0]
print(ans)