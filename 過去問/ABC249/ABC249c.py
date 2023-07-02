from collections import defaultdict


N,K = map(int,input().split())
S = [input() for _ in range(N)]
ans = 0
for bit in range(1<<N):
    cnt = defaultdict(int)
    tmp = 0
    for i in range(N):
        if bit >> i & 1:
            for s in S[i]:
                cnt[s] += 1
    for n in cnt.values():
        if n == K:
            tmp += 1
    ans = max(ans,tmp)
print(ans)