from collections import defaultdict


N = int(input())
inf = float('inf')
dmax = defaultdict(lambda:-inf)
dmin = defaultdict(lambda:inf)
for i in range(N):
    x,c= map(int,input().split())
    dmax[c] = max(dmax[c],x)
    dmin[c] = min(dmin[c],x)
dmax[0] = 0
dmin[0] = 0
dpmax = 0
dpmin = 0
pi = 0
for i in reversed(range(N+1)):
    pmax = dmax[i]
    pmin = dmin[i]
    if pmax == -inf and pmin == inf:
        continue
    n = pmax - pmin
    resmax = min(abs(pmax - dmax[pi])+dpmin,abs(pmax - dmin[pi])+dpmax) + n
    resmin = min(abs(pmin - dmax[pi])+dpmin,abs(pmin - dmin[pi])+dpmax) + n
    dpmax = resmax
    dpmin = resmin
    pi = i
print(min(dpmax,dpmin))


