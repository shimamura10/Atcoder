from collections import deque


N,D,A = map(int,input().split())
XH = [list(map(int,input().split())) for _ in range(N)]
XH.sort()
ans = 0
bomb = deque()
n = 0
for xh in XH:
    x = xh[0]
    h = xh[1]
    while bomb:
        b,c = bomb.popleft()
        if b >= x:
            bomb.appendleft((b,c))
            break
        else:
            n -= c
    h -= A*n
    if h > 0:
        c = h//A + (h%A and 1)
        n += c
        ans += c
        bomb.append((x+2*D,c))
print(ans)
