from collections import defaultdict


N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
d = defaultdict(int)
d[(0,0,0,0)] = 1
xp,ym,x,y = 0,0,0,0
ans = 0
for a in A:
    ans += d[(xp,ym,x-1,y-1)]
    if a == X:
        x += 1
        d[(xp,ym,x,y)] = d[(xp,ym,x-1,y)] + 1
    elif a == Y:
        y += 1
        d[(xp,ym,x,y)] = d[(xp,ym,x,y-1)] + 1
    elif a > X:
        xp += 1
        d[(xp,ym,x,y)] = d[(xp-1,ym,x,y)] + 1
    elif a < Y:
        ym += 1
        d[(xp,ym,x,y)] = d[(xp,ym-1,x,y)] + 1
    else:
        d[(xp,ym,x,y)] = d[(xp,ym,x,y)] + 1
ans += d[(xp,ym,x-1,y-1)]
print(ans)