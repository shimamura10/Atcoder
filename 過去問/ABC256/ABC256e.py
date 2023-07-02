from collections import defaultdict
from heapq import heappop, heappush


N = int(input())
X = list(map(int,input().split()))
C = list(map(int,input().split()))
hate = [0]*N
for i,x in enumerate(X):
    hate[x-1] += C[i]
que = []
for i,h in enumerate(hate):
    heappush(que,(h,i))
seen = [False]*N
ans = 0
while que:
    h,idx = heappop(que)
    if seen[idx]:
        continue
    seen[idx] = True
    ans += h
    ni = X[idx] -1
    if seen[ni]:
        continue
    hate[ni] -= C[idx]
    heappush(que,(hate[ni],ni))
print(ans)
    