N,K = map(int,input().split())
h = list(map(int,input().split()))
inf = 10**10
dp = [inf]*N
dp[0] = 0
for i in range(N):
    a = 0
    for k in range(min(K,i)):
        dp[i] = min(dp[i],dp[i-k-1]+abs(h[i]-h[i-k-1]))
print(dp[-1])