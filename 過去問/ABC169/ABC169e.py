N = int(input())
AB = []
for i in range(N):
    a,b = map(int,input().split())
    AB.append((a,0,i))
    AB.append((b,1,i))
AB.sort()
ans = 0
# seen = [False]*N
M = 0
m = 0
if N%2 == 1:
    md = (N+1)//2
    ok = False
    ansM = 0
    for x,ab,ind in AB:
        if ab == 0:
            M += 1
            # seen[ind] = True
        else:
            m += 1
        if M == md and not ok:
            ansm = x
            ok = True
        if ok and m == md:
            ansM = x
            break
    # if ansM == 0:
    #     ansM = AB[-1][0]
    ans = ansM - ansm + 1
else:
    md1 = N//2
    md2 = N//2+1
    ok1 = 0
    ok2 = 0
    ansM1 = 0
    ansM2 = 0
    for x,ab,ind in AB:
        if ab == 0:
            M += 1
            # seen[ind] = True
        else:
            m += 1
        if M == md1 and not ok1:
            ansm1 = x
            ok1 = 1
        if ok1 == 1 and m == md1:
            ansM1 = x
            ok1 += 1
        if M == md2 and not ok2:
            ansm2 = x
            ok2 = 1
        if ok2 == 1 and m == md2:
            ansM2 = x
            break
    # if ansM1 == 0:
    #     ansM1 = AB[-1][0]
    # if ansM2 == 0:
    #     ansM2 = AB[-1][0]
    ans = (ansM1+ansM2)-(ansm1+ansm2)+1
    # if ansM1 >= ansm2:
    #     n = ansM1 - ansm2 + 1
    #     ans -= sum(range(n))
print(ans)
    