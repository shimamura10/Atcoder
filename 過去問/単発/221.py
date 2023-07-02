from heapq import heappop, heappush


N = int(input())
ans = [0]*(N+1)
q = []
for i in range(N):
    a,b = map(int,input().split())
    heappush(q,(a,1))
    heappush(q,(a+b,-1))
n = 0
a,b = heappop(q)
d = a
n += b
i = 0
while len(q):
    a,b = heappop(q)
    # if a == d:
    #     n += b
    #     continue
    # if i == 0:
    #     ans[n-1] += d
    #     i = 1
    #     n += b
    #     d = a
    #     continue
    ans[n-1] += a-d
    n += b
    d = a
# ans[n-1] += N-d
del ans[-1]
print(*ans)