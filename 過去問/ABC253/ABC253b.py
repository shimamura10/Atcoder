H,W = map(int,input().split())
S = [input() for _ in range(H)]
n = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == 'o':
            if n == 0:
                n += 1
                sx = i
                sy = j
            else:
                nx = i
                ny = j
print(abs(sx-nx)+abs(sy-ny))
