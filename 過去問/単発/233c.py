N,X = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
# seen = [[False]*A[i][0] for i in range(N)]
k = 1
ans = 0
def dfs(x,y,k):
    # seen[x][y] = True
    nk = k*A[x][y+1]
    # print(x,y,nk)
    if x < N-1:
        for i in range(A[x+1][0]):
            dfs(x+1,i,nk)
    if x == N-1 and nk == X:
        global ans
        ans += 1
        # print(ans)

for i in range(A[0][0]):
    dfs(0,i,k)
        
print(ans)

# a = 0
# def f():
#     global a
#     a += 1
#     print(a)
# for i in range(5):
#     f()