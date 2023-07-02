X,K,D = map(int,input().split())
X = abs(X)
n = X//D
if n >= K:
    print(X-K*D)
    exit()
if (K-n)%2 == 0:
    print(X-n*D)
else:
    print((n+1)*D-X)