from collections import deque


N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [-1]*N
que = deque()
for i in G[0]:
    que.append((i,0))
while len(que):
    v,pv = que.popleft()
    if ans[v] >= 0:
        continue
    ans[v] = pv
    for nv in G[v]:
        if ans[nv] == -1:
            que.append((nv,v))
print('Yes')
for i in range(1,N):
    print(ans[i]+1)


    
