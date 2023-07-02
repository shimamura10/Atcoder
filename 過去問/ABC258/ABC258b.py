N = int(input())
A = [input() for _ in range(N)]
# for i in range(N):
#     A[i] *= 3
# A *= 3
# print(A)

ans = 0
dx = [1,1,1,0,-1,-1,-1,0]
dy = [1,0,-1,1,1,0,-1,-1]
for i in range(N):
    for j in range(N):
        for k in range(8):
            tmp = A[i][j]
            for l in range(N-1):
                i += dx[k]
                j += dy[k]
                i %= N
                j %= N
                tmp += A[i][j]
            ans = max(ans,int(tmp))
print(ans)