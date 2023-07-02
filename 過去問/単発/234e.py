S = input()
N = len(S)
X = []
for i in range(N):
    X.append(int(S[i]))
ans = [0]*N
def numfy(X):
    res = 0
    for i in range(len(X)):
        res += X[-(i+1)]*10**i
    return res

if N > 10:
    bool = True
    for i in range(N-1):
        if X[i] < X[i+1]:
            bool = False
            break
        elif X[i] > X[i+1]:
            break
    if bool:
        for i in range(N):
            ans[i] = X[0]
    else:
        for i in range(N):
            ans[i] = X[0] + 1
else:
    dmax = 10//N

    ok = True
    while not :
        d = X[0] - X[1]
        if d > dmax:
            d = dmax
        ans[0] = X[0]
        for i in range(1,N):
            ans[i] = X[i-1] - d
            if numfy(ans) < numfy(X) and ok:
                ok = False
                if X[i-1] < 9:
                    X[i-1] += 1
                
                

        



a = [3,2]
b = [6,3]
b[0] = a[0]
a[0] = 5
print(a,b)