from itertools import accumulate


N,M = map(int,input().split())
G = [[] for _ in range(M)]
right = 0
bmin = M
for _  in range(N):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    right = max(right,a)
    bmin = min(bmin,b)
    G[a].append(b)
imos = [0]*(M+1)
for left in range(bmin+1):
    if right < left:
        break
    imos[right-left] += 1
    imos[M-left] -= 1
    for b in G[left]:
        right = max(right,b)
ans = list(accumulate(imos))
del ans[-1]
print(*ans)