N = int(input())
X = []
Y = []
for i in range(N):
    x,y =map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
xm = X[(N-1)//2]
ym = Y[(N-1)//2]
ans = 0
for i in range(N):
    ans += abs(X[i]-xm) + abs(Y[i]-ym)
print(ans)