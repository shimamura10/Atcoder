N,X = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
x = 0
X *= 100
for i in range(N):
    x += A[i][0]*A[i][1]
    if x > X:
        print(i+1)
        break
if x <= X:
    print(-1)
