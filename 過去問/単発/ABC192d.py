X = input()
X = X[::-1]
M = int(input())
n = max(X) + 1
ans = 0
while True:
    tmp = 0
    for i,x in enumerate(X):
        tmp += n**i*x
    if tmp <= M:
        ans += 1
    else:
        break