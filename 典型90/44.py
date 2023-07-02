N,Q= map(int,input().split())
a = list(map(int,input().split()))
ini = 0
for i in range(Q):
    t,x,y = map(int,input().split())
    x = (x + ini -1)%N
    y = (y + ini -1)%N
    if t == 1:
        a[x],a[y] = a[y],a[x]
    if t == 2:
        ini -= 1
    if t == 3:
        print(a[x])
