s = input()
t = input()
ns = len(s)
nt = len(t)
dp = [[0]*(nt+1) for _ in range(ns+1)]
# print(dp)
# ans = []
# print(len(dp[0][0]))
for i in range(ns):
    for j in range(nt):
        if s[i] == t[j]:
            dp[i+1][j+1] = 1 + dp[i][j]
            # ans.append(s[i])
            # dp[i+1][j+1] = dp[i][j] + [s[i]]
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
            # if len(dp[i+1][j]) > len(dp[i][j+1]):
            #     dp[i+1][j+1] = dp[i+1][j]
            # else:
            #     dp[i+1][j+1] = dp[i][j+1]
# print(''.join(dp[-1][-1]))
ans = []
n = dp[-1][-1]
i = ns
j = nt
while n:
    if s[i-1] == t[j-1]:
        ans.append(s[i-1])
        n -= 1
        i -= 1
        j -= 1
    else:
        if dp[i-1][j] == dp[i][j]:
            i -= 1
        else:
            j -= 1
print(''.join(ans[::-1]))
# for i in range(nt):
#     if dp[-1][i] != dp[-1][i+1]:
#         ans.append(t[i])
# if len(ans):
#     del ans[-1]
# print(dp[-1])
# print(''.join(ans[::-1]))