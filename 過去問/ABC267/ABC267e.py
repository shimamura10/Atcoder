from heapq import heapify, heappop, heappush
N,M = map(int,input().split())
A = list(map(int,input().split()))
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
cost = []
heapcost = []
for i in range(N):
    tmp = 0
    for v in G[i]:
        tmp += A[v]
    cost.append(tmp)
    heapcost.append((tmp, i))

heapify(heapcost)
ans = 0
seen = [False]*N
while heapcost:
    c, n = heappop(heapcost)
    if (seen[n]):
        continue
    seen[n] = True
    ans = max(ans,c)
    a = A[n]
    for v in G[n]:
        cost[v] -= a
        heappush(heapcost, (cost[v],v))
print(ans)