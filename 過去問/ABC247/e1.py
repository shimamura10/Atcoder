N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
if X == Y:
    cnt = []
    tmp = 0
    for i in range(N):
        if A[i] == X:
            tmp += 1
        elif tmp:
            cnt.append(tmp)
            tmp = 0
    cnt.append(tmp)
    ans = 0
    import sys
    sys.setrecursionlimit(10000000)
    
    nCr = {}
    def cmb(n, r):
        if n < r: return 0
        if r == 0 or r == n or n == 0: return 1
        if r == 1: return n
        if (n,r) in nCr: return nCr[(n,r)]
        nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
        return nCr[(n,r)]
    for i in cnt:
        ans += cmb(i,2) + i
    print(ans)
    exit()
ans = 0
cnt = 1
cntx  = 0
cnty = 0
r = 0
for i in range(N):
    a = A[i]
    if a > X:
        cnt = 1
        cntx = 0
        cnty = 0
        r = i+1
    elif a < Y:
        cnt = 1
        cntx = 0
        cnty = 0
        r = i+1
    elif a == X:
        cntx += 1
    elif a == Y:
        cnty += 1
    while cntx >= 1 and cnty >= 1:
        if A[r] == X:
            if cntx == 1:
                break
            cntx -= 1
        elif A[r] == Y:
            if cnty == 1:
                break
            cnty -= 1
        cnt += 1
        r += 1
    if cntx >= 1 and cnty >= 1:
        ans += cnt
print(ans)