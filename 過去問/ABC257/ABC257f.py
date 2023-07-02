from collections import deque


N,M = map(int,input().split())
G = [[] for _ in range(N)]
unpair = []
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if a == -1:
        unpair.append(b)
    else:
        G[a].append(b)
        G[b].append(a)
inf = 1<<30
def shortest(s):
    q = deque()
    q.append((0,s))
    dis = [inf]*N
    seen = [False]*N
    seen[s] = True
    while q:
        c,i = q.popleft()
        dis[i] = c
        for ni in G[i]:
            if seen[ni]:
                continue
            q.append((c+1,ni))
            seen[ni] = True
    return dis
dis1 = shortest(0)
disN = shortest(N-1)
m1,mN = inf,inf
for i in unpair:
    m1 = min(m1,dis1[i])
    mN = min(mN,disN[i])
Ans = []
for i in range(N):
    ans = min(dis1[-1],min(dis1[i],m1+1)+min(disN[i],mN+1))
    if ans >= inf:
        Ans.append(-1)
    else:
        Ans.append(ans)
print(*Ans)