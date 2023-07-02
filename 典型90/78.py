N,M = map(int,input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = 0
for i in range(N):
    tmp = 0
    for j in G[i]:
        if j < i:
            tmp += 1
    if tmp == 1:
        ans += 1
print(ans)