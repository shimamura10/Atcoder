H,W = map(int,input().split())
A = [input() for _ in range(H)]
dp1 = [[0]*W for _ in range(H)]
dp2 = [[0]*W for _ in range(H)]
for i in reversed(range(H)):
    for j in reversed(range(W)):
        if i == H-1 and j == W-1:
            continue
        tmpi = -10**10
        tmpj = -10**10
        if i + 1 < H:
            if A[i+1][j] == '+':
                tmpi = dp2[i+1][j] + 1 - dp1[i+1][j]
            else:
                tmpi = dp2[i+1][j] - 1 - dp1[i+1][j]
        if j + 1 < W:
            if A[i][j+1] == '+':
                tmpj = dp2[i][j+1] + 1 - dp1[i][j+1]
            else:
                tmpj = dp2[i][j+1] - 1 - dp1[i][j+1]
        if tmpi  > tmpj:
            dp1[i][j] = tmpi + dp1[i+1][j]
            dp2[i][j] = dp1[i+1][j]
        else:
            dp1[i][j] = tmpj + dp1[i][j+1]
            dp2[i][j] = dp1[i][j+1]
if dp1[0][0] > dp2[0][0]:
    print('Takahashi')
elif dp1[0][0] < dp2[0][0]:
    print('Aoki')
elif dp1[0][0] == dp2[0][0]:
    print('Draw')