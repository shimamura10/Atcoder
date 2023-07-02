H,W,A,B = map(int,input().split())
seen = [[False]*W for _ in range(H)]
ans = 0
def dfs(A,B,i,j,k):
    if A == 0 and B == 0:
        global ans
        ans += 1
        return
    if k == 0:
        seen[i][j] = True
    elif k == 1:
        seen[i][j] = True
        seen[i+1][j] = True
    elif k == 2:
        seen[i][j] = True
        seen[i][j+1] = True
    for x in range(H):
        for y in range(W):
            if seen[x][y] == False:
                if B > 0:
                    dfs(A,B-1,x,y,0)
                if x+1 < H and seen[x+1][y] == False and A > 0:
                    dfs(A-1,B,x,y,1)
                if y+1 < W and seen[x][y+1] == False and A > 0:
                    dfs(A-1,B,x,y,2)
                seen[i][j] = False
                if k == 1:
                    seen[i+1][j] = False
                elif k == 2:
                    seen[i][j+1] = False
                return
dfs(A,B-1,0,0,0)
if H > 1:
    dfs(A-1,B,0,0,1)
if W > 1:
    dfs(A-1,B,0,0,2)
print(ans)
    

