N,D = map(int,input().split())
LR = []
for i in range(N):
    l,r = map(int,input().split())
    LR.append((l,0,i))
    LR.append((r,1,i))
LR.sort()
des = set()
tmpdes = set()
r = 0
ans = 0
for n,lr,ind in LR:
    if r > 0 and n >= r + D:
        r = 0
        des |= tmpdes
        ans += 1
        tmpdes = set()
    if lr:
        if not r and not ind in des:
            r = n
    else:
        tmpdes.add(ind)
if r:
    ans += 1
print(ans)
