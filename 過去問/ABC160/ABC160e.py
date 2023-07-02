X,Y,A,B,C = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
que = [(x,0) for x in p] + [(y,1) for y in q] + [(z,2) for z in r]
que = sorted(que,reverse=True)
a,b,c = 0,0,0
ind = 0
ans = 0
while True:
    tmp,k = que[ind]
    if k == 0:
        if a < X:
            ans += tmp
            a += 1
    elif k == 1:
        if b < Y:
            ans += tmp
            b += 1
    elif k == 2:
        ans += tmp
        c += 1
    if a + b + c == X + Y:
        break
    ind += 1
print(ans)

