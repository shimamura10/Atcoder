# for i in range(n+1):
#     for j in range(n+1):
#         for k in range(n+1):
#             s=i+j+k 
#             if s==0:
#                 dp[i][j][k]=0
#                 continue
#             dp[i][j][k]=n/s 
#             if i-1>=0:
#                 dp[i][j][k]+=dp[i-1][j+1][k]*(i/s)
#             if j-1>=0:
#                 dp[i][j][k]+=dp[i][j-1][k+1]*(j/s)
#             if k-1>=0:
#                 dp[i][j][k]+=dp[i][j][k-1]*(k/s)