N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x-y)
    Y.append(x+y)
xmin = min(X)
xmax = max(X)
ymin = min(Y)
ymax = max(Y)
print(max(abs(xmin-xmax),abs(ymin-ymax)))