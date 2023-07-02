from collections import defaultdict


N,K = map(int,input().split())
A = list(map(int,input().split()))
B = sorted(A)
P = defaultdict(lambda:defaultdict(int))
for i,b in enumerate(B):
    P[b][i%K] += 1
ok = True
for i,a in enumerate(A):
    if P[a][i%K]:
        P[a][i%K] -= 1
        continue
    ok = False
if ok:
    print('Yes')
else:
    print('No')