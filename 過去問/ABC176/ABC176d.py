from collections import deque


H,W = map(int,input().split())
sh,sw = map(int,input().split())
gh,gw = map(int,input().split())
sh -= 1
sw -= 1
gh -= 1
gw -= 1
D = [[-1]*W for _ in range(H)]
for i in range(H):
    S = input()
    for j in range(W):
        if S[j] == '#':
            D[i][j] = -2
dh = [1,0,-1,0]
dw = [0,1,0,-1]
def dfs(i,j,d):
    D[i][j] = d
    for k in range(4):
        ni = i + dh[k]
        nj = j + dw[k]
        if ni < 0 or ni >= H or nj < 0 or nj >= W:
            continue
        if D[ni][nj] == -1 and D[ni][nj] != -2:
            dfs(ni,nj,d)
flag = 0
for i in range(H):
    for j in range(W):
        if D[i][j] == -1:
            dfs(i,j,flag)
            flag += 1
edge = [set() for _ in range(flag)]
for i in range(H):
    for j in range(W):
        for k in range(max(0,i-2),min(H,i+3)):
            for l in range(max(0,j-2),min(W,j+3)):
                if D[i][j] == -2 or D[k][l] == -2:
                    continue
                edge[D[i][j]].add(D[k][l])
                edge[D[k][l]].add(D[i][j])
start = D[sh][sw]
goal = D[gh][gw]
dist = [-1]*flag
dist[start] = 0
que = deque()
que.append(start)
while len(que) != 0:
    v = que.popleft()
    for nv in edge[v]:
        if nv == v or nv == -2 or dist[nv] != -1 :
            continue
        dist[nv] = dist[v] + 1
        que.append(nv)
print(dist[goal])
print(D)
print(edge)
# stack = {(sh,sw)}
# d = 0
# ns = []
# while True:
#     i,j = stack.pop()
#     if D[i][j] == -1:
#         dfs(i,j,d)
#     if len(stack) == 0:
#         for k,l in ns:
#             for m in range(max(0,k-2),min(H,k+3)):
#                 for n in range(max(0,l-2),min(W,l+3)):
#                     if D[m][n] == -1:
#                         stack.add((m,n))
#         d += 1
#     if len(stack) == 0:
#         break
# print(D[gh][gw])

