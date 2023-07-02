from collections import deque


N = int(input())
G = [[] for _ in range(N)]
canput = deque()
seen = [False]*N
for i in range(N):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(i)
    G[b].append(i)
    if i == a:
        canput.append(i)
        seen[i] = True
    elif i == b:
        canput.append(i)
        seen[i] = True
ans = []
while canput:
    i = canput.popleft()
    ans.append(i)
    for ni in G[i]:
        if not seen[ni]:
            canput.append(ni)
            seen[ni] = True
if len(ans) == N:
    for a in ans[::-1]:
        print(a+1)
else:
    print(-1)