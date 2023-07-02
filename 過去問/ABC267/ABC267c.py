N,M = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for i in range(M):
    ans += A[i] * (i+1)
tmp = ans
l = sum(A[:M])
for i in range(M,N):
    tmp += A[i] * M
    tmp -= l
    l += A[i] - A[i-M]
    ans = max(ans,tmp)
print(ans)
