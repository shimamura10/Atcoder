A,B = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
dp1 = [[0]*(B+1) for _ in range(A+1)]
dp2 = [[0]*(B+1) for _ in range(A+1)]
dp1[1][0] = a[A-1]
dp1[0][1] = b[B-1]
for i in range(2,A+1):
    dp1[i][0] = dp1[i-2][0] + a[A-i]
    dp2[i][0] = dp2[i-2][0] + a[A-i+1]
for i in range(2,B+1):
    dp1[0][i] = dp1[0][i-2] + b[B-i]
    dp2[0][i] = dp2[0][i-2] + b[B-i+1]
for i in range(A):
    for j in range(B):
        # dp1[i+1][j+1] = max(dp2[i][j+1] + a[i],dp2[i+1][j] + b[j])
        # dp2[i+1][j+1] = max(dp1[i][j+1],dp1[i+1][j])
        if dp2[i][j+1] + a[A-i-1] > dp2[i+1][j] + b[B-j-1]:
            dp1[i+1][j+1] = dp2[i][j+1] + a[A-i-1]
            dp2[i+1][j+1] = dp1[i][j+1]
        else:
            dp1[i+1][j+1] = dp2[i+1][j] + b[B-j-1]
            dp2[i+1][j+1] = dp1[i+1][j]
print(dp1[A][B])
# print(dp1)
# print(dp2)