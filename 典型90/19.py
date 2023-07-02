N = int(input())
A = list(map(int,input().split()))
dp = [[0]*(2*N+1) for _ in range(2*N)]
for k in range(1,N+1):
    for l in range(2*N):
        r = l + 2*k
        if r > 2*N:
            break
        tmp = abs(A[l] - A[r-1])
        tmp += dp[l+1][r-1]
        for i in range(1,k):
            tmp = min(tmp,dp[l][l+2*i]+dp[l+2*i][r])
        dp[l][r] = tmp
print(dp[0][2*N])