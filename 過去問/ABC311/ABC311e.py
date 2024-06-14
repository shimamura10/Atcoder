H,W,N = map(int,input().split())
A = [[1]*(W+1) for _ in range(H+1)]
for _ in range(N):
  a,b = map(int,input().split())
  # a -= 1
  # b -= 1
  A[a][b] = 0
dp = [[0]*(W+1) for _ in range(H+1)]
for i in range(1,H+1):
  for j in range(1,W+1):
    if A[i][j] == 0:
      continue
    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
print(sum([sum(a) for a in dp]))
# for i in range(H+1):
#   A[i][0] = 0
# for j in range(W+1):
#   A[0][j] = 0
# for i in range(H):
#   for j in range(W+1):
#     A[i+1][j] += A[i][j]
# for i in range(H+1):
#   for j in range(W):
#     A[i][j+1] += A[i][j]
# def binary_search(function,no,ok,i,j):  #mが条件を満たすかどうかを返す関数function
#     while True:                     #条件を満たさない値no
#         m = (no + ok)//2            #条件を満たす値ok
#         if function(i,j,m):             #ギリギリ条件を満たすindexを返す
#             ok = m
#         else:
#             no = m
#         if abs(ok - no) == 1:
#             return ok
# def hasNoHole(i,j,n):
#   if i+n-1 > H or j+n-1 > W or n == 0:
#     return False
#   num = A[i+n-1][j+n-1] - A[i+n-1][j-1] - A[i-1][j+n-1] + A[i-1][j-1]
#   if num == n*n:
#     return True
#   else:
#     return False
# ans = 0
# M = max(H+1,W+1)
# for i in range(1,H+1):
#   for j in range(1,W+1):
#     maxn = binary_search(hasNoHole, M, 0, i, j)
#     ans += maxn
# print(ans)