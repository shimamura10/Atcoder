N,W = map(int,input().split())
ans = 'Yes'
time = 0
import heapq
q = []
for i in range(N):
    s,t,p = map(int,input().split())
    q.append((s,p))
    q.append((t,-p))
heapq.heapify(q)
p = 0
while len(q) != 0:
    p += heapq.heappop(q)[1]
    if p > W:
        ans = 'No'
        break
print(ans)