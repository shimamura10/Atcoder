from heapq import heapify, heappop, heappush


N,L = map(int,input().split())
A = list(map(int,input().split()))
if L != sum(A):
    A.append(L-sum(A))
heapify(A)
ans = 0
while len(A) > 1:
    a = heappop(A)
    b = heappop(A)
    ans += a+b
    heappush(A,a+b)
print(ans)