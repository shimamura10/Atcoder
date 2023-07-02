N,M = map(int,input().split())
A = list(map(int,input().split()))
A = A[::-1]
C = list(map(int,input().split()))
C = C[::-1]
B = []
for i in range(M+1):
    re = 0
    for k in range(i):
        if i - k >= 0 and i - k < N + 1:
            re += B[k]*A[i-k]
    b = (C[i] - re)//A[0]
    B.append(b)
print(*B[::-1])
