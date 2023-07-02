N = int(input())
p = [[0]*1001 for _ in range(1001)]
for _ in range(N):
    lx,ly,rx,ry = map(int,input().split())
    p[lx][ly] += 1
    p[lx][ry] -= 1
    p[rx][ly] -= 1
    p[rx][ry] += 1
for i in range(1001):
    for j in range(1000):
        p[i][j+1] += p[i][j]
for j in range(1001):
    for i in range(1000):
        p[i+1][j] += p[i][j]
ans = [0]*(N+1)
for i in range(1001):
    for j in range(1001):
        ans[p[i][j]] += 1
del ans[0]
for a in ans:
    print(a)
