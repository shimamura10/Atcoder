from collections import deque
import sys
sys.setrecursionlimit(100000000)
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

H,W = map(int,input().split())
S = [input() for _ in range(H)]
D = [[-1]*W for _ in range(H)]
q = deque()
dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,1,-1,1,-1]
q.append((0,0,0))
while D[-1][-1] == -1 and len(q):
    sx,sy,n = q.popleft()
    D[sx][sy] = n
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if S[nx][ny] == '#':
            if D[nx][ny] == -1:
                q.append((nx,ny,n+1))
                D[nx][ny] = n+1
            for j in range(8):
                nnx = nx + dx[j]
                nny = ny + dy[j]
                if nnx < 0 or nnx >= H or nny < 0 or nny >= W or D[nnx][nny] != -1:
                    continue
                if S[nnx][nny] == '#' and D[nnx][nny] == -1:
                    q.append((nnx,nny,n+1))
                    D[nnx][nny] = n+1
        elif S[nx][ny] == '.' and D[nx][ny] == -1:
            q.appendleft((nx,ny,n))
print(D[-1][-1])
