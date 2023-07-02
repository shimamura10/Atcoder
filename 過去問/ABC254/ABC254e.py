from collections import deque


N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
Q = int(input())
for _ in range(Q):
    x,k = map(int,input().split())
    x -= 1
    seen = set()
    stack = deque()
    stack.append((x,0))
    ans = 0
    while stack:
        x,d = stack.popleft()
        # ans += x+1
        seen.add(x)
        if d == k:
            continue
        for nx in G[x]:
            if nx in seen:
                continue
            stack.append((nx,d+1))
    for a in seen:
        ans += a+1
    print(ans)
    
    