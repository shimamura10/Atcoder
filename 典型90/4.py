H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
gyou = [0]*H
retu = [0]*W
for i in range(H):
    for j in range(W):
        gyou[i] += A[i][j]
        retu[j] += A[i][j]
ans = [[gyou[i] + retu[j] - A[i][j] for j in range(W)] for i in range(H)]
for a in ans:
    print(*a)

