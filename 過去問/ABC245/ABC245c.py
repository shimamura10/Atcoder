N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = True
b = True
for i in range(N-1):
    na = False
    nb = False
    if a:
        if abs(A[i+1]-A[i]) <= K:
            na = True
        if abs(B[i+1]-A[i]) <= K:
            nb = True
    if b:
        if abs(A[i+1]-B[i]) <= K:
            na = True
        if abs(B[i+1]-B[i]) <= K:
            nb = True
    a = na
    b = nb
if a or b:
    print('Yes')
else:
    print('No')