N,M,X = map(int,input().split())
C = []
A = []
for _ in range(N):
    a = list(map(int,input().split()))
    C.append(a[0])
    A.append(a[1:])
inf = float('inf')
ans = inf
for bit in range(1<<N):
    tmp = 0
    tmpA = [0]*M
    for i in range(N):
        if bit >> i & 1:
            tmp += C[i]
            for j in range(M):
                tmpA[j] += A[i][j]
    ok = True
    for j in range(M):
        if tmpA[j] < X:
            ok = False
    if ok:
        ans = min(ans,tmp)
if ans == inf:
    print(-1)
else:
    print(ans)
            
