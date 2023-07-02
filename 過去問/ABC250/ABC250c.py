from collections import defaultdict


N,Q = map(int,input().split())
ans = [i+1 for i in range(N)]
pos = defaultdict(int)
for a in ans:
    pos[a] = a-1
for _ in range(Q):
    x = int(input())
    p = pos[x]
    if p == N-1:
        ans[p],ans[p-1] = ans[p-1],ans[p]
        pos[ans[p-1]] = p-1
        pos[ans[p]] = p
    else:
        ans[p],ans[p+1] = ans[p+1],ans[p]
        pos[ans[p]] = p
        pos[ans[p+1]] = p + 1
print(*ans)