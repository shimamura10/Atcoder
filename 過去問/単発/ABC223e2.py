X,Y,A,B,C = map(int,input().split())
def f2(X,Y,A,B):
    if X <= 0 or Y <= 0:
        return False
    if A%X == 0:
        ya = A//X
    else:
        ya = A//X + 1
    if B%X == 0:
        yb = B//X
    else:
        yb = B//X + 1
    if ya + yb <= Y:
        return True
    if A%Y == 0:
        ya = A//Y
    else:
        ya = A//Y + 1
    if B%Y == 0:
        yb = B//Y
    else:
        yb = B//Y + 1
    if ya + yb <= X:
        return True
    return False
def f(A,B,C):
    if A%X == 0:
        ya = A//X
    else:
        ya = A//X + 1
    if f2(X,Y-ya,B,C):
        print('Yes')
        exit()
    if A%Y == 0:
        ya = A//Y
    else:
        ya = A//Y + 1
    if f2(X-ya,Y,B,C):
        print('Yes')
        exit()
f(A,B,C)
f(B,C,A)
f(C,A,B)
print('No')
    