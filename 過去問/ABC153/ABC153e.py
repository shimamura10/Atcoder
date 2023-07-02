H,N = map(int,input().split())
A = []
B = []
for _ in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
dp = [10**9]*(H+1)
dp[0] = 0
for i in range(N):
    a = A[i]
    b = B[i]
    for j in range(1,H+1):
        dp[j] = min(dp[j],dp[max(0,j-a)]+b)
print(dp[H])