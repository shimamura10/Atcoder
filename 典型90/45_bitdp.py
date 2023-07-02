N,K = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(N)]
dis = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dis[i][j] = (P[i][0]-P[j][0])**2 + (P[i][1]-P[j][1])**2
D = [0]*2**N
for bit in range(2**N):
    tmp = 0
    for i in range(N):
        if bit >> i & 1:
            tmp = D[bit - (1<<i)]
            for j in range(i+1,N):
                if bit >> j & 1:
                    tmp = max(tmp,dis[i][j])
            break
    D[bit] = tmp
inf = float('inf')
# ans = [[D[bit]] + [inf]*(K-1) for bit in range(2**N)]
ans = [D] + [[inf]*(1<<N) for _ in range(K-1)]
for k in range(1,K):
    for bit in range(1<<N):
        s = bit
        while s:
            # ans[bit][k] = min(ans[bit][k],max(D[s],ans[bit-s][k-1]))
            ans[k][bit] = min(ans[k][bit],max(D[s],ans[k-1][bit-s]))
            s = (s-1) & bit
# for bit in range(2**N):
#     exists = []
#     for i in range(N):
#         if bit >> i & 1:
#             exists.append(i)
#     s_list = []
#     for bitbit in range(2**len(exists)):
#         s = 0
#         for j in range(len(exists)):
#             if bitbit >> j & 1:
#                 s += 1 << exists[j]
#         s_list.append(s)
#     for k in range(1,K):
#         tmp = inf
#         for s in s_list:
#             tmp = min(tmp,max(D[s],ans[bit-s][k-1]))
#         ans[bit][k] = tmp
print(ans[-1][-1])
print(2**15*15*15)