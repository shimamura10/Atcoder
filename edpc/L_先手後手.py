N = int(input())
A = list(map(int,input().split()))
dp = [[0]*N for _ in range(N)]
# dp[N-1][N-1] = A[N-1]
for i in reversed(range(N)):
    for j in range(N):
        if i > j:
            continue
        if i == j:
            dp[i][j] = A[i]
            continue
        a,b =0,0
        if j-1>= 0 and i <= j-1:
            a = A[j] - dp[i][j-1]
        if i + 1 < N and i+1 <= j:
            b = A[i] - dp[i+1][j]
        dp[i][j] = max(a,b)
print(dp[0][N-1])
# print(dp)