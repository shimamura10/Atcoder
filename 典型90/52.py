N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
mod = 10**9+7
dp = [[0]*6 for _ in range(N)]
def dfs(i,j):
    if dp[i][j] != 0:
        return dp[i][j]
    res = 0
    if i < N-1:
        for k in range(6):
            res += dfs(i+1,k)*A[i][j]
    else:
        res = A[i][j]
    res %= mod
    dp[i][j] = res
    return res
ans = 0
for i in range(6):
    ans += dfs(0,i)
print(ans%mod)