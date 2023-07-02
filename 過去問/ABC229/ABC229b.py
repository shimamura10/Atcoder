A,B = input().split()
for i in range(min(len(A),len(B))):
    a = int(A[-(i+1)])
    b = int(B[-(i+1)])
    if a + b >= 10:
        print('Hard')
        exit()
print('Easy')
