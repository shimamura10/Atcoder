N = int(input())
A = list(map(int,input().split()))

serial = [0]
for i in range(N-1):
    serial.append(serial[i] + A[i//2])
dp = [0]*(N+1)
for i in range(N):
    for j in range(N):
        if i + j + 1 > N:
            break
        dp[i+j+1] = max(dp[i+j+1], dp[i] + serial[j])
print(dp[N])