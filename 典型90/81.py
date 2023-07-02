N,K = map(int,input().split())
A = [[0]*5000 for _ in range(5000)]
n = 0
for i in range(N):
    a,b = map(int,input().split())
    n = max(n,a,b)
    a -= 1
    b -= 1
    A[a][b] += 1
for i in range(n):
    for j in range(n-1):
        A[i][j+1] += A[i][j]
for j in range(n):
    for i in range(n-1):
        A[i+1][j] += A[i][j]
ans = 0
for i in range(n):
    for j in range(n):
        ri = min(n-1,i+K)
        rj = min(n-1,j+K)
        if i > 0:
            a = A[i-1][rj]
        else:
            a = 0
        if j > 0:
            b = A[ri][j-1]
        else:
            b = 0
        if i == 0 or j == 0:
            c = 0
        else:
            c = A[i-1][j-1]
        tmp = A[ri][rj] - a - b + c
        ans = max(ans,tmp)
print(ans)