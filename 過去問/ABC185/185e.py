N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = i
for j in range(M+1):
    dp[0][j] = j
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            a = 0
        else:
            a = 1
        dp[i+1][j+1] = min(dp[i+1][j]+1,dp[i][j+1]+1,dp[i][j]+a)
print(dp[N][M])
# dp = [0]*(M+1)
# dp[0] = N
# for j in range(1,M+1):
#     if dp[j-1] < 0:
#         dp[j-1] = 0
#     if N < j:
#         dp[j] = dp[j-1]+1
#     else:
#         dp[j] = dp[j-1]
#         if A[j-1] == B[j-1]:
#             dp[j] -= 1
#             continue
#     if A[N-1] == B[j-1]:
#         dp[j] -= 1
# print(dp[M])
# print(1<<20)