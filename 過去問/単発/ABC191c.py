H,W = map(int,input().split())
S = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            sx = i-1
            sy = j-1
dx = [1,0,-1,0]
dy = [0,1,0,-1]
tx = sx
ty = sy
ans = 0
di = 1
while True:
    nx = tx + dx[di]
    ny = ty + dy[di]


