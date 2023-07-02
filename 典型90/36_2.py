N,Q = map(int,input().split())
X = []
Y = []
for _ in range(N):
    x,y = map(int,input().split())
    X.append(x-y)
    Y.append(x+y)
MX = max(X)
mX = min(X)
MY = max(Y)
mY = min(Y)
for _ in range(Q):
    q = int(input())
    q -= 1
    x = max(X[q]-mX,MX-X[q])
    y = max(Y[q]-mY,MY-Y[q])
    print(max(x,y))