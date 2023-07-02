from collections import defaultdict


H,W = map(int,input().split())
S = [input() for _ in range(H)]
mod = 10**9 + 7
D = [[0]*W for _ in range(H)]
D[0][0] = 1
yoko = [0 for _ in range(W)]
tate = [0 for _ in range(H)]
naname = defaultdict(int)
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            yoko[j] = 0
            tate[i] = 0
            naname[i-j] = 0
            continue
        D[i][j] += tate[i] + yoko[j] + naname[i-j]
        D[i][j] %= mod
        yoko[j] += D[i][j]
        tate[i] += D[i][j]
        naname[i-j] += D[i][j]
print(D[-1][-1])