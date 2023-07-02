from collections import defaultdict


N,M = map(int,input().split())
ac = defaultdict(int)
wa = defaultdict(int)
for _ in range(M):
    p,s = input().split()
    if s == 'WA' and ac[p] == 0:
        wa[p] += 1
    if s == 'AC':
        ac[p] += 1
accnt = 0
wacnt = 0
for key in ac.keys():
    if ac[key] == 0:
        continue
    accnt += 1
    wacnt += wa[key]
print(*[accnt,wacnt])