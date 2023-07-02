# a = [1,2,3]
# b = a
# a[0] = 2
# print(b)

n = int(input())
mod = 998244353
num = [[0]*9 for _ in range(n)]
for i in range(9):
    num[0][i] = 1
for i in range(n-1):
    num[i+1][0] = (num[i][0] + num[i][1])%mod
    num[i+1][8] = (num[i][8] + num[i][7])%mod
    for j in range(1,8):
        num[i+1][j] = (num[i][j-1] + num[i][j] + num[i][j+1])%mod
    # print(num)
print(sum(num[-1])%mod)
