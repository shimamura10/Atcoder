from collections import defaultdict


N,M = map(int,input().split())
S = list(map(int,input().split()))
X = list(map(int,input().split()))
tmp = [0]
for s in S:
    tmp.append(s-tmp[-1])
cnt = defaultdict(int)
for i,t in enumerate(tmp):
    if i%2:
        for x in X:
            cnt[x-t] += 1
    else:
        for x in X:
            cnt[t-x] += 1
ans = 0
for a in cnt.values():
    ans = max(ans,a)
print(ans)
