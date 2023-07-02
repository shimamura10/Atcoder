a,b,c = map(int,input().split())
A = [a,b,c]
A.sort()
if b == A[1]:
    print('Yes')
else:
    print('No')