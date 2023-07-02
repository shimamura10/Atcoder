from collections import deque


N = int(input())
ax,ay = map(int,input().split())
bx,by = map(int,input().split())
S = [input() for _ in range(N)]
# A = [[0]*(N+1) for _ in range(N+1)]
# for i in range(N):
#     tmp = 0
#     for j in range(N):
#         if S[i][j] == '#':
#             tmp += 1
#         A[i+1][j+1] = tmp
# for j in range(N):
#     for i in range(N-1):
#         A[i+2][j+1] += A[i+1][j+1]

q = deque()
seen = [[10**7]*N for _ in range(N)]
seen[ax-1][ay-1] = 0
q.append((ax,ay))
while len(q):
    i,j = q.popleft()
    for d in range(1,min(N-i+1,N-j+1)):
        if S[i+d-1][j+d-1] =='#' or seen[i+d-1][j+d-1] <= seen[i-1][j-1]:
            break
        else:
            if seen[i+d-1][j+d-1] == seen[i-1][j-1] + 1:
                continue
            seen[i+d-1][j+d-1] = seen[i-1][j-1] + 1
            q.append((i+d,j+d))
    for d in range(1,min(i,N-j+1)):
        if S[i-d-1][j+d-1] == '#' or seen[i-d-1][j+d-1] <= seen[i-1][j-1]:
            break
        else:
            if seen[i-d-1][j+d-1] == seen[i-1][j-1] + 1:
                continue
            seen[i-d-1][j+d-1] = seen[i-1][j-1] + 1
            q.append((i-d,j+d))
    for d in range(1,min(N-i+1,j)):
        if S[i+d-1][j-d-1] == '#' or seen[i+d-1][j-d-1] <= seen[i-1][j-1]:
            break
        else:
            if seen[i+d-1][j-d-1] == seen[i-1][j-1] + 1:
                continue
            seen[i+d-1][j-d-1] = seen[i-1][j-1] + 1
            q.append((i+d,j-d))
    for d in range(1,min(i,j)):
        if S[i-d-1][j-d-1] == '#' or seen[i-d-1][j-d-1] <= seen[i-1][j-1]:
            break
        else:
            if seen[i-d-1][j-d-1] == seen[i-1][j-1] + 1:
                continue
            seen[i-d-1][j-d-1] = seen[i-1][j-1] + 1
            q.append((i-d,j-d))
if seen[bx-1][by-1] == 10**7:
    print(-1)
else:
    print(seen[bx-1][by-1])
