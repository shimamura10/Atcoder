N = int(input())
A = list(map(int,input().split()))
dp = [[-1]*N for _ in range(N)]
accum = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        tmp = 0
        for k in range(i,j+1):
            tmp += A[k]
        accum[i][j] = tmp
for i in range(N):
    dp[i][i] = 0
def dfs(i,j):
    if dp[i][j] != -1:
        return dp[i][j]
    res = 10**16
    for k in range(i,j):
        res = min(res,dfs(i,k) + dfs(k+1,j))
    res += accum[i][j]
    dp[i][j] = res
    return res
print(dfs(0,N-1))
