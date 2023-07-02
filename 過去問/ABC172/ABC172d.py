from itertools import accumulate


N = int(input())
ans = 0
sum = list(accumulate(range(N+1)))
for i in range(1,N+1):
    ans += sum[N//i]*i
print(ans)

