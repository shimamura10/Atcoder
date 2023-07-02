Q = int(input())
b = []
u = []
for i in range(Q):
    t,x = map(int,input().split())
    if t == 1:
        u.append(x)
    elif t ==  2:
        b.append(x)
    else:
        if x <= len(u):
            print(u[-x])
        else:
            print(b[x-len(u)-1])