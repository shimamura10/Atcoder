N,S = map(int,input().split())
cost = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    a,b = cost[i-1]
    for j in range(S+1):
        if j - a >= 0 and dp[i-1][j-a]:
            dp[i][j] = 1
        elif j - b >= 0 and dp[i-1][j-b]:
            dp[i][j] = 1
if dp[-1][-1] == 0:
    print("Impossible")
    exit()
ans = ""
s = S
for i in range(N):
    a,b = cost[N-i-1]
    if s-a >= 0 and dp[N-i-1][s-a]:
        ans += "A"
        s -= a
    elif s-b >= 0 and dp[N-i-1][s-b]:
        ans += "B"
        s -= b
print(ans[::-1])
