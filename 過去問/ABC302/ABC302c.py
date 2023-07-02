from itertools import permutations


N,M = map(int,input().split())
S = [input() for _ in range(N)]
def count_chrnum(A,B):
    cnt = 0
    b_list = [b for b in B]
    for a in A:
        issame = False
        for bnum in range(len(b_list)):
            if a == b_list[bnum]:
                issame = True
                del b_list[bnum]
                break
        # if not issame:
        #     cnt += 1
    cnt = len(b_list)
    return cnt
edge = [[] for _ in range(N)]
isedge = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if count_chrnum(S[i],S[j]) == 1:
            edge[i].append(j)
            edge[j].append(i)
            isedge[i][j] = True
            isedge[j][i] = True
for p in permutations(range(N)):
    for i in range(N-1):
        if not isedge[p[i]][p[i+1]]:
            break
        if i == N-2:
            print('Yes')
            exit()
print('No')

# def dfs(i):
#     seen[i] = True
#     if sum(seen) == len(seen):
#         print("Yes")
#         exit()
#     for ni in edge[i]:
#         if seen[ni]:
#             continue
#         dfs(ni)
#     seen[i] = False
# for s in range(N):
#     seen = [False]*N
#     dfs(s)
# print("No")
