N,K = map(int,input().split())
K += 1
C = 5001
place = [[0]*C for _ in range(C)]
A,B = 0,0
for _ in range(N):
    a,b = map(int,input().split())
    place[a][b] += 1
    A = max(A,a)
    B = max(B,b)
for i in range(C):
    for j in range(C-1):
        place[i][j+1] += place[i][j]
for j in range(C):
    for i in range(C-1):
        place[i+1][j] += place[i][j]
ans = 0
for a in range(K,C):
    for b in range(K,C):
        tmp = place[a][b] - place[a-K][b] - place[a][b-K] + place[a-K][b-K]
        ans = max(ans,tmp)
print(ans)