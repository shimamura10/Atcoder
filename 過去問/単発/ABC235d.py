from collections import deque


a,N = map(int,input().split())
q = deque()
q.append((1,0))
seen = set()
while len(q):
    x,n = q.popleft()
    if x == N:
        print(n)
        exit()
    if a*x < N*10:
        nx = a*x
        if not(nx in seen):  
            seen.add(nx)
            q.append((nx,n+1))
    sx = str(x)
    if len(sx) > 1 and x%10 != 0:
        nx = int(sx[-1]+sx[:len(sx)-1])
        if not(nx in seen):
            seen.add(nx)
            q.append((nx,n+1))
print(-1)

