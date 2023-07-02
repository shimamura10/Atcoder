from itertools import accumulate


N = int(input())
ans = [0]*(3*10**5)
for i in range(N):
    x,y = map(int,input().split())
    ans[x] += 1
    ans[y] -= 1
ans = list(accumulate(ans))
ok = False
l = 0
r = 0
for i,a in enumerate(ans):
    if ok:
        if a <= 0:
            r = i
            print(*[l,r])
            ok = False
    else:
        if a > 0:
            l = i
            ok = True

