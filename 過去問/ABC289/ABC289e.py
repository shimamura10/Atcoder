from collections import deque


T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    C = list(map(int,input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    next = deque()
    next.append((0,N-1,0))
    seen = [[False]*N for _ in range(N)]
    seen[0][N-1] = True
    ok = True
    G2 = [[]for _ in range(N**2)]
    cnt = 0
    # for a in range(N):
    #     for na in G[a]:
    #         for b in range(N):
    #             for nb in G[b]:
    #                 if C[na] + C[nb] == 1:
    #                     G2[a*N+b].append((na,nb))
    while next:
        a,b,t = next.popleft()
        if a == N-1 and b == 0:
            print(t)
            ok = False
            break
        for na in G[a]:
            for nb in G[b]:
                cnt += 1
                if not seen[na][nb] and C[na] + C[nb] == 1:
                    next.append((na,nb,t+1))
                    seen[na][nb] = True
        # for na,nb in G2[a*N+b]:
        #     if not seen[na][nb]:
        #         next.append((na,nb,t+1))
        #         seen[na][nb] = True
    if ok:
        print(-1)
    # print(cnt)