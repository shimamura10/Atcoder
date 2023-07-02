# ans = 1
# for i in range(8):
#     ans *= 2*i+1
# print(ans)

# print(bin(10))
# print(4^1)

# import itertools
# import math
N = int(input())
A = [list(map(int,input().split())) for _ in range(2*N-1)]
# L = []
# for i in range(N):
#     L.extend([i,i+1])
# c_list = list(itertools.combinations(L,2))
# N_c = len(c_list)

# ans = 0
# i = 0
# while i < N:
#     ind = 0
#     for j in range(2*N):
#         if not seen[j]:
#             ind = j
#             break
# Ans = [0]*N
# while len(c_list) > 0:
#     for i in range(N):
#         c_list = list(itertools.combinations(L,2))
#         a = c_list[i][0]
#         b = c_list[i][1]
#         del c_list[i]
#         seen[a] = True
#         seen[b] = True
#         ans = A[a][b]
#         while ind2 < N-1:
#             ind = 0
#             ind2 = 0
#             while seen[a] or seen[b]:
#                 a = c_list[ind][0]
#                 b = c_list[ind][1]
#                 ind += 1
#                 # if ind > len(c_list-1):
#                 #     break
#             seen[a] = True
#             seen[b] = True
#             ans ^= A[a][b]
#             ind2 += 1
#             del c_list[-1]

Ans = [0]
def dfs(a,ans,n):
    # print(a,b,seen,ans,n)
    if n == N:
        Ans[0] = max(Ans[0],ans)
        return
    for i in range(a+1,2*N):
        if not seen[i]:
            seen[i] = True
            break
    for j in range(i+1,2*N):
        if not seen[j]:
            seen[j] = True
            dfs(i,ans^A[i][j-i-1],n+1)
            seen[j] = False
    seen[i] = False

seen = [False]*2*N
dfs(-1,0,0)

print(Ans[0])

# a = [False]*5
# n = 0
# b = 0
# def f(a,n,b):
#     a[n] = True
#     n+= 1
#     b = 5
# f(a,0,b)
# print(a,b)


    

        
