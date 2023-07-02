from collections import defaultdict, deque


N = int(input())
P = list(map(int,input().split()))
I = list(map(int,input().split()))
if P[0] != 1:
    print(-1)
    exit()
pos = defaultdict(int)
for i,a in enumerate(I):
    pos[a] = i
ans = [[0,0] for i in range(N)]
que = deque()
que.append((0,N,0,N))
while que:
    pl,pr,il,ir = que.popleft()
    par = P[pl]
    idxpar = pos[par]
    if idxpar < il or idxpar >= ir:
        print(-1)
        exit()
    if idxpar != il:
        que.append((pl+1,pl+idxpar-il+1,il,idxpar))
        ans[par-1][0] = P[pl+1]
    if idxpar != ir-1:
        que.append((pl+idxpar-il+1,pr,idxpar+1,ir))
        ans[par-1][1] = P[pl+idxpar-il+1]
for a in ans:
    print(*a)
