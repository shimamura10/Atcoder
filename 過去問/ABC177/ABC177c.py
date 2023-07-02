from itertools import accumulate


N = int(input())
A = list(map(int,input().split()))
sum = list(accumulate(A))
ans = 0
mod = 10**9 + 7
for i in range(1,N):
    ans = (ans + sum[i-1]*A[i])%mod
print(ans)