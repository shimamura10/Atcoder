from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
cnt = defaultdict(int)
for a in A:
    cnt[a] += 1
s = 0
ans = 0
for n in cnt.values():
    ans += n*s*(N-s-n)
    s += n
print(ans)