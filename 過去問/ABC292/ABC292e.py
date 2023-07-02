from collections import deque


N,M = map(int,input().split())
G = [[] for _ in range(N)]
# Gbool = [[False]*N for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    # Gbool[a][b] = True
# ad = [[[] for _ in range(N)] for _ in range(N)]
# q = []
# for a in range(N):
#     for b in G[a]:
#         for c in range(N):
#             if Gbool[a][c]:
#                 continue
#             if Gbool[b][c]:
#                 q.append((a,c))
#             else:
#                 ad[b][c].append((a,c))
#             if Gbool[c][a]:
#                 q.append((c,b))
#             else:
#                 ad[c][a].append((c,b))
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
ans = 0
for i in range(N):
    for d in shortest(i):
        if d != inf and d > 1:
            ans += 1
print(ans)