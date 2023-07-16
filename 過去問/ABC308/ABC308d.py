H, W = map(int,input().split())
S = [input() for _ in range(H)]
nextvistit = {'s':'n', 'n':'u', 'u':'k', 'k':'e', 'e':'s'}
canvistit = []
visited = [[False]*W for _ in range(H)]
if (S[0][0] == 's'):
  canvistit.append((0,0))
  visited[0][0] = True
di = [0,0,1,-1]
dj = [1,-1,0,0]
while canvistit:
  i,j = canvistit.pop()
  if i == H-1 and j == W-1:
    print('Yes')
    exit()
  for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]
    if ni < 0 or ni >= H or nj < 0 or nj >= W:
      continue
    if S[ni][nj] == nextvistit[S[i][j]] and visited[ni][nj] == False:
      canvistit.append((ni, nj))
      visited[ni][nj] = True
print('No')