import sys
sys.setrecursionlimit(100000000)
N = int(input())
C = list(input().split())
G = [[] for _ in range(N)]
mod = 10**9 + 7
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
dp = [[-1,-1,-1] for _ in range(N)]
def dfs(i,j,pi):
    if dp[i][j] >= 0:
        return dp[i][j]
    if C[i] == 'a':
        cnum = 0
    else:
        cnum = 1
    if j == 1-cnum:
        dp[i][j] = 0
        return 0
    elif j == cnum:
        ans = 1
        for chi in G[i]:
            if chi == pi:
                continue
            # i-chiの辺を切ったらchiの部分木はa,b両方持ってる必要があり、切らなかったらa(or b)のみ持ってる必要がある。
            ans = ans*(dfs(chi,cnum,i) + dfs(chi,2,i))%mod
        dp[i][cnum] = ans
    else:
        ans = 1
        for chi in G[i]:
            if chi == pi:
                continue
            # とりあえずi以外で条件満たすやつ全部足す
            # i-chiの辺を切ったらchiの部分木はa,b両方持ってる必要があり、切らなかったら他の子との兼ね合いで満たす可能性あるから全部ok
            ans = ans*(dfs(chi,0,i) + dfs(chi,1,i) + 2*dfs(chi,2,i))%mod
        # iを含む部分木がa (or b)のみ持ってる場合を引く
        ans -= dfs(i,cnum,pi)
        ans %= mod
        dp[i][2] = ans
    return ans
ans = dfs(0,2,0)
print(ans)