X,Y = map(int,input().split())
if Y%2 == 1:
    print('No')
    exit()
if Y >= 2*X and Y<= 4*X:
    print('Yes')
else:
    print('No')