N,K = map(int,input().split())
T = [list(map(int,input().split())) for _ in range(N)]
import itertools
l = [i for i in range(1,N)]
P = list(itertools.permutations(l,len(l)))
# print(len(P))
# l.append(0)
ans = 0
for p in P:
    time = 0
    for i in range(N):
        if i == 0:
            time += T[0][p[i]]
        elif i == N-1:
            time += T[p[i-1]][0]
        else:
            time += T[p[i-1]][p[i]]
    if time == K:
        ans += 1
print(ans)

# l = [i for i in range(1,4)]
# P = list(itertools.permutations(l,len(l)))
# print(P)
    

