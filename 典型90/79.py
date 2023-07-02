H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
B = [list(map(int,input().split())) for _ in range(H)]
for i in range(H):
    for j in range(W):
        A[i][j] -= B[i][j]
ans = 0
for i in range(H-1):
    for j in range(W-1):
        a = A[i][j]
        ans += abs(a)
        A[i+1][j] -= a
        A[i][j+1] -= a
        A[i+1][j+1] -= a
if A[-1][-1] == 0 and A[-1][-2] == 0 and A[-2][-1] == 0:
    print('Yes')
    print(ans)
else:
    print('No')