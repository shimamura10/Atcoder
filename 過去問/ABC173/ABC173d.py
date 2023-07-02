from heapq import heapify, heappop, heappush
a = heapify([1,3])
print(type(a))
print(heappop(a))

N = int(input())
A = list(map(int,input().split()))
A = sorted(A,reverse=True)
q = [(-A[0],-A[0])]
ans = 0
for i in range(1,N):
    a = heappop(q)
    ans -= a[0]
    heappush(q,(-A[i],a[0]))
    heappush(q,(-A[i],a[1]))
print(ans)