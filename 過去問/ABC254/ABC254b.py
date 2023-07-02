N = int(input())
ans = [[1]*(i+1) for i in range(N)]
for i in range(N):
    for j in range(1,i):
        ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
    print(*ans[i])