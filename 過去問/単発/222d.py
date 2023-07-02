N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [[0]*(b[-1]+1) for _ in range(N+1)]
mod = 998244353
for i in range(a[0],b[0]+1):
    dp[1][i] = i+1-a[0]
for i in range(2,N+1):
    for j in range(a[i-1],b[i-1]+1):
        dp[i][j] = (dp[i-1][min(j,b[i-2])] + dp[i][j-1])%mod
print(dp[-1][-1])
# print(dp)