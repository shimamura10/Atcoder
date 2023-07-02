N,Q = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(Q)]
mod = 1000000007
ans = 0
for i in range(60):
    tmp = 0
    for bit in range(1<<N):
        ok = True
        for x,y,z,w in C:
            if (bit >> x-1 | bit >> y-1 | bit >> z-1)%2 != (w>>i)%2:
                ok = False
                break
        if ok:
            tmp += 1
    if ans == 0:
        ans = tmp
    else:
        ans = (ans*tmp)%mod
print(ans)
