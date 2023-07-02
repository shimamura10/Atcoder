N,K = map(int,input().split())
A = list(map(int,input().split()))
dp = [-1]*(K+1)
dp[0] = 0
for i in range(1,K+1):
    if dp[i] == -1:
        tmp = 0
        for a in A:
            if i - a >= 0 and dp[i-a] == 0:
                tmp = 1
                break
        dp[i] = tmp
if dp[K] == 1:
    print('First')
else:
    print('Second')
