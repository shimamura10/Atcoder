N,K = map(int,input().split())
K += 1
C = 5001
place = [[0]*C for _ in range(C)]
A,B = 0,0
for _ in range(N):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    place[a][b] += 1
    A = max(A,a)
    B = max(B,b)

colom = [0]*C
for a in range(C):
    for b in range(K):
        colom[a] += place[a][b]
ans = 0
for b in range(C-K):
    if b > 0:
        for a in range(C):
            colom[a] += place[a][b+K-1]
            colom[a] -= place[a][b-1]
    tmp = 0
    for a in range(K):
        tmp += colom[a]
    ans = max(ans,tmp)
    for a in range(C-K):
        tmp += colom[K+a]
        tmp -= colom[a]
        ans = max(ans,tmp)
print(ans)