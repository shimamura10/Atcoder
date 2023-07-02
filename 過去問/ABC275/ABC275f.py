N,M = map(int,input().split())
A = list(map(int,input().split()))
inf = 10**4
dp = [[inf for _ in range(M+1)] for _ in range(N)]
canunuse = [[1 for _ in range(M+1)] for _ in range(N)]
dp[0][0] = 1
canunuse[0][0] = 0
if A[0] <= M:
    dp[0][A[0]] = 0
    canunuse[0][A[0]] = 1
for i in range(1,N):
    for j in range(M+1):
        unuse = dp[i-1][j] + canunuse[i-1][j]
        use = inf
        if j >= A[i]:
            use = dp[i-1][j-A[i]]
        if min(use, unuse) == inf:
            continue
        if use <= unuse:
            dp[i][j] = use
        if unuse <= use:
            dp[i][j] = unuse
            canunuse[i][j] = 0
for j in range(1,M+1):
    ans = dp[-1][j]
    if ans == inf:
        print(-1)
    else:
        print(ans)