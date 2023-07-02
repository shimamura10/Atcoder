from itertools import permutations


# ans = 1
# for i in range(1,11):
#     ans *= i
# print(ans)
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
M = int(input())
# B = [list(map(int,input().split())) for _ in range(M)]
G = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
# print(G)
ans = 10000
for v in permutations(range(N)):
    b = False
    for i in range(N-1):
        if v[i+1] in G[v[i]]:
            # print(v,i)
            b = True
            break
    if b:
        continue
    # print(v)
    res = 0
    for i in range(N):
        res += A[v[i]][i]
    ans = min(res,ans)
if ans != 10000:
    print(ans)
else:
    print(-1)