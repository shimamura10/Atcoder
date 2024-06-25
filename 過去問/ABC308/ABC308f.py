from heapq import heapify, heappop, heappush


N,M = map(int,input().split())
class qupon():
  def __init__(self, l, d):
    self.limit = l
    self.discount = d
P = list(map(int,input().split()))
L = list(map(int,input().split()))
D = list(map(int,input().split()))
P.sort()
qupons = [qupon(L[i], D[i]) for i in range(M)]
qupons.sort(key=lambda x:x.limit)
q = 0
canUse = [] 
heapify(canUse)
ans = sum(P)
for p in P:
  if q < M and p >= qupons[q].limit:
    while True:
      heappush(canUse,-qupons[q].discount)
      q += 1
      if q == M or qupons[q].limit > p:
        break
  if canUse:
    ans += heappop(canUse)
print(ans)