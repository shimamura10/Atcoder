N,K = map(int,input().split())
A = list(map(int,input().split()))
B = sorted(A+[0])
ans = K//N
K %= N
idx = B[K]
for a in A:
    if a <= idx:
        print(ans+1)
    else:
        print(ans)