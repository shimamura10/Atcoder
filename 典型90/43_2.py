from collections import deque


H,W = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
sx -= 1
sy -= 1
gx -= 1
gy -= 1
S = [input() for _ in range(H)]
dp = [[[10**7]*4 for _ in range(W)] for _ in range(H)]
q = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(4):
    q.append((sx,sy,i,0))
    # dp[sx][sy][i] = 0
while q:
    x,y,d,n = q.popleft()
    if n >= dp[x][y][d]:
        continue
    dp[x][y][d] = n
    if x == gx and gy == y:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if S[nx][ny] == '#':
            continue
        if i == d:
            if dp[nx][ny][i] <= dp[x][y][d]:
                continue
            # dp[nx][ny][i] = dp[x][y][d]
            q.appendleft((nx,ny,i,dp[x][y][d]))
        else:
            if dp[nx][ny][i] <= dp[x][y][d] + 1:
                continue
            # dp[nx][ny][i] = dp[x][y][d] + 1
            q.append((nx,ny,i,dp[x][y][d]+1))
ans = 10**7
for i in range(4):
    ans = min(ans,dp[gx][gy][i])
print(ans)