H,W = map(int,input().split())
S = [input() for _ in range(H)]
target = 'snuke'
kouho = []
route = []
dx = [1,1,0,-1,-1,-1,0,1]
dy = [0,1,1,1,0,-1,-1,-1]
def dfs(i,j,n):
    if S[i][j] == target[n]:
        route.append([i+1,j+1])
        if n == len(target)-1:
            for r in route:
                print(*r)
            exit()
        for d in range(8):
            ni = i + dx[d]
            nj = j + dy[d]
            if ni < 0 or ni == H or nj < 0 or nj == W:
                continue
            dfs(ni,nj,n+1)
        del route[-1]
            
# for i in range(H):
#     for j in range(W):
#         dfs(i,j,0)

for i in range(H):
    for j in range(W):
        for d in range(8):
            ni = i
            nj = j
            for n in range(5):
                if ni < 0 or ni == H or nj < 0 or nj == W:
                    break
                if S[ni][nj] != target[n]:
                    break
                ni += dx[d]
                nj += dy[d]
                if n == 4:
                    for a in range(5):
                        print(*[i+dx[d]*a+1,j+dy[d]*a+1])