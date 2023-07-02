T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    ans = -10**10
    tmp = 0
    acc = 0
    for i in range(N):
        x,y = map(int,input().split())
        if i == 0:
            ans = x
        if x < 0 and acc > -x:
            n = acc//abs(x)
            if n < y:
                tmp += acc*n + x*n*(n+1)//2
                y -= n
                acc += x*n
                ans = max(ans,tmp)
        tmp += acc*y + x*y*(y+1)//2
        acc += x*y
        ans = max(ans,tmp)
    print(ans)
