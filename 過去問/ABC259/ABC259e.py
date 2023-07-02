from collections import defaultdict


N = int(input())
pdict = defaultdict(lambda:[0])
A = []
for _ in range(N):
    m = int(input())
    a = []
    for j in range(m):
        p,e = map(int,input().split())
        pdict[p].append(e)
        a.append([p,e])
    A.append(a)
for p in pdict.keys():
    pdict[p].sort()
S = set()
ans = 0
for a in A:
    tmp = []
    for p,e in a:
        if pdict[p][-1] == e and e-pdict[p][-2] > 0:
            tmp += [p,e-pdict[p][-2]]
    tupletmp = tuple(tmp)
    if not(tupletmp in S):
        ans += 1
        S.add(tupletmp)
print(ans)