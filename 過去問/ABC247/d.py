from collections import deque


Q = int(input())
q = deque()
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        q.append((query[1],query[2]))
    else:
        ans = 0
        n = query[1]
        while n > 0:
            x,c = q.popleft()
            if c <= n:
                n -= c
                ans += x*c
            else:
                ans += x*n
                q.appendleft((x,c-n))
                n = 0
        print(ans)