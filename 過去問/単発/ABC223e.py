from math import sqrt


X,Y,A,B,C = map(int,input().split())
if A%X == 0:
    ya = A//X
else:
    ya = A//X + 1
if B%X == 0:
    yb = B//X
else:
    yb = B//X + 1
if C%X == 0:
    yc = C//X
else:
    yc = C//X + 1
if ya + yb + yc <= Y:
    print('Yes')
    exit()
if Y-ya != 0:
    if B%(Y-ya) == 0:
        yb = B//(Y-ya)
    else:
        yb = B//(Y-ya) + 1
    if C%(Y-ya) == 0:
        yc = C//(Y-ya)
    else:
        yc = C//(Y-ya) + 1
    if yb + yc <= X:
        print('Yes')
        exit()
if A%Y == 0:
    ya = A//Y
else:
    ya = A//Y + 1
if B%Y == 0:
    yb = B//Y
else:
    yb = B//Y + 1
if C%Y == 0:
    yc = C//Y
else:
    yc = C//Y + 1
if ya + yb + yc <= X:
    print('Yes')
    exit()
if X-ya != 0:
    if B%(X-ya) == 0:
        yb = B//(X-ya)
    else:
        yb = B//(X-ya) + 1
    if C%(X-ya) == 0:
        yc = C//(X-ya)
    else:
        yc = C//(X-ya) + 1
    if yb + yc <= Y:
        print('Yes')
        exit()

if B > C:
    B,C = C,B
max = int(sqrt(A)) + 1
def binary_search(function,no,ok):  #mが条件を満たすかどうかを返す関数function
    while True:                     #条件を満たさない値no
        m = (no + ok)//2            #条件を満たす値ok
        if function(m):             #ギリギリ条件を満たさないindexを返す
            ok = m
        else:
            no = m
        if abs(ok - no) == 1:
            return ok
def f(x):
    if A%x == 0:
        y = A//x
    else:
        y = A//x + 1
    b = x*(Y-y)
    if b >= B:
        return True
    else:
        return False
x = binary_search(f,1,A)
if A%x == 0:
    y = A//x
else:
    y = A//x + 1
c = (X-x)*Y
b = x*(Y-y)
if (c >= B and b >= C) or (b >= B and c >= C):
    print('Yes')
    exit()
def f1(x):
    if A%x == 0:
        y = A//x
    else:
        y = A//x + 1
    b = X*(Y-y)
    if b >= B:
        return True
    else:
        return False
x = binary_search(f1,1,A)
if A%x == 0:
    y = A//x
else:
    y = A//x + 1
c = (X-x)*y
b = X*(Y-y)
if (c >= B and b >= C) or (b >= B and c >= C):
    print('Yes')
    exit()




# for x in range(1,max+1):
#     if A%x == 0:
#         y = A//x
#     else:
#         y = A//x + 1
#     b = (X-x)*Y
#     c = x*(Y-y)
#     d = (X-y)*Y
#     e = y*(Y-x)
#     if f(b,c) or f(d,e):
#         print('Yes')
#         exit()
print('No')
    


    