from collections import deque


N,M = map(int,input().split())
A = list(map(int,input().split()))
seen = [0]*N
a = sorted(A[:M])
for i in a:
    seen[i] += 1
for i in range(N+1):
    if i == N:
        ans = N
        break
    if seen[i] == 0:
        ans = i
        break
a = deque(A[:M])
for i in range(N-M):
    l = a.popleft()
    seen[l] -= 1
    seen[A[M+i]] += 1
    a.append(A[M+i])
    if seen[l] == 0:
        ans = min(ans,l)
print(ans)
