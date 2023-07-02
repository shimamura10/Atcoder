from collections import defaultdict


N,K = map(int,input().split())
A = list(map(int,input().split()))
k = 0
cnt = defaultdict(int)
l = 0
n = 0
ans = 0
for a in A:
    if cnt[a] == 0:
        k += 1
    cnt[a] += 1
    n += 1
    while k > K:
        n -= 1
        cnt[A[l]] -= 1
        if cnt[A[l]] == 0:
            k -= 1
        l += 1
    ans = max(ans,n)
print(ans)