N,Q = map(int,input().split())
A = [0]*N
for _ in range(Q):
    n,x = map(int,input().split())
    x -= 1
    if n != 3:
        A[x] += n
    else:
        if A[x] >= 2:
            print("Yes")
        else:
            print("No")