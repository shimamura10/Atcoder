import sys
sys.setrecursionlimit(100000000)
N = int(input())
a = list(map(int,input().split()))
i,j,k = 0,0,0
for l in range(N):
    if a[l] == 1:
        i += 1
    if a[l] == 2:
        j += 1
    if a[l] == 3:
        k += 1
dp = [[[-1]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 0
def dfs(i,j,k):
    if i == -1 or j == -1 or k == -1 or i == N+1 or j == N+1 or k == N+1:
        return 0
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    n = i+j+k
    res = N/n
    res += i/n*dfs(i-1,j,k)
    res += j/n*dfs(i+1,j-1,k)
    res += k/n*dfs(i,j+1,k-1)
    dp[i][j][k] = res
    return res
print(dfs(i,j,k))
