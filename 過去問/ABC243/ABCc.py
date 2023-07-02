
N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
S = input()
A = []
for i in range(N):
    A.append([Y[i],X[i],S[i]])
A.sort()
y,x,s = A[0]
i = 1
b = [[x,s]]
while i < N:
    if y == A[i][0]:
        b.append([A[i][1],A[i][2]])
    else:
        b.sort()
        ok = False
        for j in b:
            if j[1] == 'R' and not(ok):
                ok = True
            if j[1] == 'L' and ok:
                print('Yes')
                exit()
        y = A[i][0]
        b = [[A[i][1],A[i][2]]]
    i += 1
b.sort()
ok = False
for j in b:
    if j[1] == 'R' and not(ok):
        ok = True
    if j[1] == 'L' and ok:
        print('Yes')
        exit()
print('No')