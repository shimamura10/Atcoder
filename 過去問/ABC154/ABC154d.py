from itertools import accumulate


N,K = map(int,input().split())
p = list(map(int,input().split()))
A = list(accumulate(range(1001)))
for i in range(1,1001):
    A[i] /= i
ans = 0
for i in range(K):
    ans += A[p[i]]
tmp = ans
for i in range(K,N):
    tmp += A[p[i]]
    tmp -= A[p[i-K]]
    ans = max(ans,tmp)
print(ans)