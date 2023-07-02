N,P,K = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
def f(x):
    es = []
    for i in range(N):
        for j in range(N):
            if A[i][j] > 0:
                es.append((i,j,A[i][j]))
            elif A[i][j] == -1:
                es.append((i,j,x))
    inf = float('inf')
    d = [[inf] * N for _ in range(N)]
    for a, b, c in es:  #esはエッジ
        d[a][b] = c
        d[b][a] = c
    next = [[j for j in range(N)] for _ in range(N)]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    next[i][j] = next[i][k]

    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if i == j:
                continue
            if d[i][j] <= P:
                cnt += 1
    return cnt
l = 1
r = 10**10
while True:
    m = (l+r)//2
    if f(m) <= K:
        r = m
    else:
        l = m + 1
    if l == r:
        break
min = l
l = 1
r = 10**10
while True:
    m = (l+r)//2
    if f(m) < K:
        r = m
    else:
        l = m + 1
    if l == r:
        break
max = l
if max == 10**10:
    if min == 10**10:
        print(0)
    else:
        print('Infinity')
else:
    print(max-min)

