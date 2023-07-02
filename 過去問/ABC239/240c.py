N,X = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(N)]
b = []

# print(dp)
for i in range(N):
    X -= ab[i][0]
    b.append(ab[i][1]-ab[i][0])

if X >= 0:
    dp = [[True]+[False]*(X) for _ in range(N+1)]
    for i in range(N):
        for k in range(X+1):
            # print(k,b[i])
            if k - b[i] >= 0:
                dp[i+1][k] = dp[i+1][k] or dp[i][k-b[i]]
            dp[i+1][k] = dp[i+1][k] or dp[i][k]
    # print(dp)
    if dp[N][X]:
        print('Yes')
    else:
        print('No')
else:
    print('No')