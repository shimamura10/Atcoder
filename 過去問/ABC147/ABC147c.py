N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append([list(map(int,input().split())) for _ in range(a)])
ans = N
for i in range(N):
    seen = [-1]*N
    seen[i] = 1
    ok = True
    q = [i]
    while q:
        j = q.pop()
        for x,y in A[j]:
            x -= 1
            if y == 1:
                if seen[x] == 0:
                    ok = False
                    break
                elif seen[x] == -1:
                    seen[x] = 1
                    q.append(x)
            else:
                if seen[x] == 1:
                    ok = False
                    break
                else:
                    seen[x] = 0
        