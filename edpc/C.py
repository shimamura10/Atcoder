N = int(input())
dp = [[0]*3 for _ in range(N+1)]
for i in range(N):
    a = list(map(int,input().split()))
    for j in range(3):
        dp[i+1][j] = a[j] + max(dp[i][j-1],dp[i][j-2])
print(max(dp[-1]))