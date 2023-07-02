import bisect
H,W,N,M = map(int,input().split())
light = [list(map(int,input().split())) for _ in range(N)]
block = [list(map(int,input().split())) for _ in range(M)]
A = [[0,W+1] for _ in range(H)]
B = [[0,H+1] for _ in range(W)]
seen = [[False]*W for _ in range(H)]
for i in range(M):
    A[block[i][0]-1].append(block[i][1])
    B[block[i][1]-1].append(block[i][0])
    seen[block[i][0]-1][block[i][1]-1] = True
for i in range(H):
    A[i].sort()
for i in range(W):
    B[i].sort()
C = [[False]*(len(A[i])-1) for i in range(H)]
D = [[False]*(len(B[i])-1) for i in range(W)]
for i in range(N):
    x = light[i][0]
    y = light[i][1]
    D[y-1][bisect.bisect_left(B[y-1],x)-1] = True
    C[x-1][bisect.bisect_left(A[x-1],y)-1] = True
ans = 0
for i in range(H):
    for j in range(W):
        if seen[i][j]:
            continue
        # i += 1
        # j += 1
        if D[j][bisect.bisect_left(B[j],i+1)-1]:
            ans += 1
            continue
        if C[i][bisect.bisect_left(A[i],j+1)-1]:
            ans += 1
print(ans)
# print(D)
# print(C)
# import bisect
# a = [1,3,5,7]
# print(bisect.bisect_left(a,2))