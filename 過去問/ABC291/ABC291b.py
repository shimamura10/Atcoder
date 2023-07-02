N = int(input())
X = list(map(int,input().split()))
X.sort()
del X[:N]
del X[-N:]
print(sum(X)/(3*N))