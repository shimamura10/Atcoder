import sys
sys.setrecursionlimit(100000000)
H,W = map(int,input().split())
S = [input() for _ in range(H)]
dp = [[-1]*W for _ in range(H)]
dpx = [[-1]*W for _ in range(H)]
dpy = [[-1]*W for _ in range(H)]
dpz = [[-1]*W for _ in range(H)]
mod = 10**9 + 7
# for i in range(H):
#     for j in range(W):
#         if S[i][j] == '#':
#             dp[i][j] = -1
dp[H-1][W-1] = 1
# if S[H-2][W-1] == '.':
#     dp[H-2][W-1] = 1
# if S[H-1][W-2] == '.':
#     dp[H-1][W-2] = 1
# if S[H-2][W-2] == '.':
#     dp[H-2][W-2] = 1
# print(dp)
def dfs(i,j):
    # print(i,j)
    if dp[i][j] != -1:
        return dp[i][j]
    res = 0
    if i+1 < H and S[i+1][j] == '.':
        res += dfs(i+1,j) + 
        if i+2 < H and S[i+2][j] == '.':
            res += dfs(i+2,j)
    if j+1 < W and S[i][j+1] == '.':
        res += dfs(i,j+1)
        if j+2 < W and S[i][j+2] == '.':
            res += dfs(i,j+2)
    if i+1 < H and j+1 < W and S[i+1][j+1] == '.':
        res += dfs(i+1,j+1)
        if i+2 < H and j+2 < W and S[i+2][j+2] == '.':
            res += dfs(i+2,j+2) 
    for k in range(i+1,H):
        if S[k][j] == '.':
            res += dfs(k,j)
            # print('a',k,j) 
        else:
            break
    for k in range(j+1,W):
        if S[i][k] == '.':       
            res += dfs(i,k) 
            # print('b',i,k)
        else:
            break
    for k in range(1,min(H-i,W-j)):
        if S[i+k][j+k] == '.':
            res += dfs(i+k,j+k)
            # print('c',i+k,j+k) 
        else:
            break
    res %= mod
    dp[i][j] = res
    # print(dp)
    return res
print(dfs(0,0))
print(dp)
