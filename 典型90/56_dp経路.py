N,S = map(int,input().split())
A,B = [],[]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
dpA = [[False]*(S+1) for _ in range(N+1)]
dpB = [[False]*(S+1) for _ in range(N+1)]
dpA[0][0] = True
dpB[0][0] = True
for i in range(N):
    for j in range(S):
        if j+1-A[i] >= 0:
            dpA[i+1][j+1] = dpA[i][j+1-A[i]] or dpB[i][j+1-A[i]]
        if j+1-B[i] >= 0:
            dpB[i+1][j+1] = dpA[i][j+1-B[i]] or dpB[i][j+1-B[i]]
if not dpA[N][S] and not dpB[N][S]:
    print('Impossible')
    exit()
ans = []
for i in range(N,0,-1):
    if dpA[i][S]:
        ans.append('A')
        S -= A[i-1]
    elif dpB[i][S]:
        ans.append('B')
        S -= B[i-1]
print(''.join(ans[::-1]))
