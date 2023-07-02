A = [list(map(int,input().split())) for _ in range(3)]
N = int(input())
seen = [[False]*3 for _ in range(3)]
for _ in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                seen[i][j] = True
ok = False
for i in range(3):
    if sum(seen[i]) == 3:
        ok = True
for j in range(3):
    tmp = 0
    for i in range(3):
        tmp += seen[i][j]
    if tmp == 3:
        ok = True
tmp1 = True
tmp2 = True
for i in range(3):
    tmp1 = tmp1 and seen[i][i]
    tmp2 = tmp2 and seen[2-i][i]
ok = tmp1 or tmp2 or ok
if ok:
    print('Yes')
else:
    print('No')