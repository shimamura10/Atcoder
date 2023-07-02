H,W = map(int,input().split())
C = [input() for _ in range(H)]
seen = [[False]*W for _ in range(H)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
def dfs(x,y,n,sx,sy):
    if n != 0:
        seen[x][y] = True
    if x == sx and y == sy and n != 0:
        return n
    n += 1
    res = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= H or ny < 0 or ny >= W:
            continue
        if not(seen[nx][ny]) and C[nx][ny] == '.':
            res = max(res,dfs(nx,ny,n,sx,sy)) 
    seen[x][y] = False
    return res
ans = 0
for x in range(H):
    for y in range(W):
        if C[x][y] == '#':
            continue
        ans = max(ans,dfs(x,y,0,x,y))
if ans <= 2:
    print(-1)
else:
    print(ans)
