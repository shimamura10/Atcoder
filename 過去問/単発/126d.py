N = int(input())
A = [list(map(int,input().split())) for i in range(N-1)]
color = [0]*N
Odd = [[] for i in range(N)]
Even = [[] for i in range(N)]
if N > 1:
    for i in range(N-1):
        if A[i][2]%2 == 1:
            Odd[A[i][0]-1].append(A[i][1]-1)
            Odd[A[i][1]-1].append(A[i][0]-1)
        else:
            Even[A[i][0]-1].append(A[i][1]-1)
            Even[A[i][1]-1].append(A[i][0]-1)

def dfs(n,col):
    color[n] = col
    for i in Odd[n]:
        if i == n:
            continue
        dfs(i,1-col)
    for i in Even[n]:
        if i == n:
            continue
        dfs(i,col)

dfs(0,0)

for i in range(N):
    print(color[i])

for i in []:
    print('a')
    print(i)
