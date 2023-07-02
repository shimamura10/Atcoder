from collections import deque


N = int(input())
ax,ay = map(int,input().split())
ax -= 1
ay -= 1
bx,by = map(int,input().split())
bx -= 1
by -= 1
S = [input() for _ in range(N)]
# G = [[[[] for _ in range(4)] for _ in range(N)] for _ in range(N)]
dx = [1,1,-1,-1]
dy = [1,-1,1,-1]
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni = i + dx[k]
#             nj = j + dy[k]
#             if ni < 0 or ni >= N or nj < 0 or nj >= N or S[ni][nj] == '#':
#                 continue
#             for l in range(4):
#                 if k == l:
#                     G[i][j][l].append((ni,nj,k,0))
#                 else:
#                     G[i][j][l].append((ni,nj,k,1))
q = deque()
inf = float('inf')
D = [[[inf]*4 for _ in range(N)] for _ in range(N)]
for i in range(4):
    q.append((ax,ay,i))
    D[ax][ay][i] = 1
while len(q):
    i,j,k = q.popleft()
    for l in range(4):
        ni = i + dx[l]
        nj = j + dy[l]
        if ni < 0 or ni >= N or nj < 0 or nj >= N or S[ni][nj] == '#':
            continue
        if k == l:
            if D[ni][nj][l] > D[i][j][k]:
                D[ni][nj][l] = D[i][j][k] 
                q.appendleft((ni,nj,l))
        else:
            if D[ni][nj][l] > D[i][j][k] + 1:
                D[ni][nj][l] = D[i][j][k] + 1
                q.append((ni,nj,l))
ans = inf
for i in range(4):
    ans = min(ans,D[bx][by][i])
if ans == inf:
    print(-1)
else:
    print(ans)