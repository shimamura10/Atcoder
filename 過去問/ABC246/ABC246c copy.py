N,K,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    n = A[i]//X
    if n <= K:
        A[i] -= X*n
        K -= n
    else:
        A[i] = A[i] - K*X
        K = 0
# if N <= K:
#     print(0)
#     exit()
A = sorted(A,reverse=True)
# print(sum(A[K:]))
ans = 0
for i,a in enumerate(A):
    if i >= K:
        ans += a
    else:
        if a > X:
            A[10**7]
print(ans)