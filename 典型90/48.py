from heapq import heappop, heappush


N,K = map(int,input().split())
q = []
for i in range(N):
    a,b = map(int,input().split())
    heappush(q,-(a-b))
    heappush(q,-b)
ans = 0
while K:
    a = heappop(q)
    K -= 1
    ans -= a
print(ans)