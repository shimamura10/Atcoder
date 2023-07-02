import itertools
N,M = map(int,input().split())
T = [list(map(int,input().split())) for i in range(M)]
A = [list(map(int,input().split())) for i in range(M)]
Tg = [[False]*N for i in range(N)]
Ag = [[False]*N for i in range(N)]

for i in range(M):
    Tg[T[i][0]-1][T[i][1]-1] = True
    Tg[T[i][1]-1][T[i][0]-1] = True
    Ag[A[i][0]-1][A[i][1]-1] = True
    Ag[A[i][1]-1][A[i][0]-1] = True
# print(Tg)
# print(Ag)
for p in itertools.permutations(range(N)):
    ans = 'Yes'
    for i in range(N):
        for j in range(N):
            if Tg[i][j] != Ag[p[i]][p[j]]:
                ans = 'No'
                break
        else:
            continue
        break
    if ans == 'Yes':
        break
print(ans)
