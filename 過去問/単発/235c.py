N,Q = map(int,input().split())
A = list(map(int,input().split()))
xk = [list(map(int,input().split())) for i in range(Q)]
dict = {}
for i in range(N):
    dict[A[i]] = []
for i in range(Q):
    dict[xk[i][0]] = []
for i in range(N):
    dict[A[i]].append(i+1)
for i in range(Q):
    if len(dict[xk[i][0]])>=xk[i][1]:
        print(dict[xk[i][0]][xk[i][1]-1])
    else:
        print(-1)

# dict1 = {}
# # dict1[1] = [1,3]
# dict1[1] += [5]
# print(dict1[1])