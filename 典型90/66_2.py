N = int(input())
LR = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(1,N):
    for j in range(i):
        ex = 0
        l,r = LR[j]
        n = r-l+1
        for k in range(LR[i][0], LR[i][1]+1):
            if k < l:
                ex += 1
            elif l <= k and k <= r:
                ex += (r-k)/n
        ex /= (LR[i][1]-LR[i][0]+1)
        ans += ex
print(ans)