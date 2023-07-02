from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
seen = defaultdict(list)
cnt = defaultdict(int)
poped = defaultdict(int)
dif = 0
for i in range(N//2+1):
    a = A[i]
    dif += cnt[a]
    seen[a].append(i)
    cnt[a] += i+1
for i in range(N//2+1,N):
    a = A[i]
    while len(seen[a]) > 0 and seen[a][-1] >= N-i:
        left = seen[a].pop()
        poped[a] += 1
        cnt[a] -= left+1
    dif += poped[a]*(N-i)
    dif += cnt[a]
    poped[a] += 1
ans = 0
for i in range(N):
    ans += (N-i)*((i+1)//2)
print(ans-dif)