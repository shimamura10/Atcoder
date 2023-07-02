import sys
sys.setrecursionlimit(1000000)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
# print(G)
list = [0]*N
def dfs(i,pi):
    res = 0
    for j in G[i]:
        if j == pi:
            continue 
        res += dfs(j,i)
    if G[i] == [pi]:
        res = 1
    list[i] = res
    return res
dfs(0,0)
# rmax = 0
L = [0]*N
R = [0]*N
L[0] = 1
R[0] = list[0]
def dfs2(i,pi):
    Lmin = L[i]
    # R[i] = L[pi] + list[i] - 1
    for j in G[i]:
        if j == pi:
            continue
        L[j] = Lmin
        R[j] = L[j] + list[j] - 1
        Lmin = R[j] + 1
        dfs2(j,i)
dfs2(0,0)
from collections import deque
Q = deque()
# Q.append(0)

# rmax = 0
# print('a')
# seen = [False]*N
# while len(Q) > 0:
#     # print(Q)
#     i = Q.popleft()
#     seen[i] = True
#     L[i] = rmax + 1
#     R[i] = L[i] + list[i] - 1
#     # Q.extend(G[i])
#     for j in G[i]:
#         # print(i)
#         if seen[j]:
#             continue
#         Q.append(j)
#     rmax = R[i]
#     if rmax == R[0]:
#         rmax = 0
    
#     if len(Q) > 5:
#         break
for i in range(N):
    print(L[i],R[i])
# a = 9
# b = 3
# print(a,b)

# from collections import deque
# Q = deque()
# Q.append(3)
# Q.append(5)
# Q.popleft()
# print(Q)
