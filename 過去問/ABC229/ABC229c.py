N,W = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB = sorted(AB,reverse=True)
ans = 0
for a,b in AB:
    if b <= W:
        ans += a*b
        W -= b
    else:
        ans += a*W
        break
print(ans)