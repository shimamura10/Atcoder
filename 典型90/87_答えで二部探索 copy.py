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
def binary_search(function,no,ok):  #mが条件を満たすかどうかを返す関数function
    while True:                     #条件を満たさない値no
        m = (no + ok)//2            #条件を満たす値ok
        if function(m):             #ギリギリ条件を満たさないindexを返す
            ok = m
        else:
            no = m
        if abs(ok - no) == 1:
            return ok
def fmin(x):
    if f(x) > K:
        return True
    else:
        return False
def fmax(x):
    if f(x) >= K:
        return True
    else:
        return False
min = binary_search(fmin,10**10,0)
max = binary_search(fmax,10**10,0)
if max > 10**9:
    if min > 10**9:
        print(0)
    else:
        print('Infinity')
else:
    print(max-min)

