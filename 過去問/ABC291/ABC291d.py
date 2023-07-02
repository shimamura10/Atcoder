mod = 998244353
from collections import defaultdict


N = int(input())
cnt = defaultdict(int)
AB = [list(map(int,input().split())) for _ in range(N)]
a,b = 1,1
for i in range(1,N):
    na = 0
    nb = 0
    if AB[i-1][0] != AB[i][0]:
        na += a
    if AB[i-1][0] != AB[i][1]:
        nb += a
    if AB[i-1][1] != AB[i][1]:
        nb += b
    if AB[i-1][1] != AB[i][0]:
        na += b
    a = na % mod
    b = nb % mod
print((a+b)%mod)
