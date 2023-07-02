from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
cnt = defaultdict(int)
for a in A:
    cnt[a] += 1
cnt2 = []
s = 0
ns = 0
ans = 0
for n in cnt.values():
    ns += n*s
    cnt2.append(ns)
    s += n
i = 0
for n in cnt.values():
    if i >= 2:
        ans += n*cnt2[i-1]
    i += 1
print(ans)