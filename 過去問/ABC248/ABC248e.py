from collections import defaultdict
from itertools import combinations

N,K = map(int,input().split())
X = []
Y = []
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
if K == 1:
    print('Infinity')
    exit()
inf = 10**10
seen = set()
ans = 0
for i in range(N):
    x = X[i]
    y = Y[i]
    d = defaultdict(list)
    for j in range(N):
        if i == j:
            continue
        if X[j] == x:
            d[inf].append(j)
        else:
            a = (Y[j]-y)/(X[j]-x)
            d[a].append(j)
    for v in d.values():
        if len(v) >= K - 1:
            if not (i,v[0]) in seen:
                ans += 1
                for a in combinations(v + [i],2):
                    seen.add(a)
print(ans)