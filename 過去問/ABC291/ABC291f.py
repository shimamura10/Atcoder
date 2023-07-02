from collections import deque


N,M = map(int,input().split())
G = [[] for _ in range(N)]
Grev = [[] for _ in range(N)]
for i in range(N):
    s = input()
    for j in range(M):
        if s[j] == '1':
            G[i].append(i+j+1)
            Grev[i+j+1].append(i)
dis = [-1]*N
seen = [False]*N
seen[0] = True
stack = deque()
stack.append((0,0))
while stack:
    i,n = stack.popleft()
    dis[i] = n
    for ni in G[i]:
        if seen[ni]:
            continue
        stack.append((ni,n+1))
        seen[ni] = True
disrev = [-1]*N
seenrev = [False]*N
seenrev[-1] = True
stackrev = deque()
stackrev.append((N-1,0))
while stackrev:
    i,n = stackrev.popleft()
    disrev[i] = n
    for ni in Grev[i]:
        if seenrev[ni]:
            continue
        stackrev.append((ni,n+1))
        seenrev[ni] = True
inf = 10**7
for k in range(1,N-1):
    ans = inf
    for i in range(max(0,k-M+1),k):
        for j in G[i]:
            if j > k and dis[i] >= 0 and disrev[j] >= 0:
                ans = min(ans,dis[i]+disrev[j]+1)
    if ans == inf:
        print(-1)
    else:
        print(ans)