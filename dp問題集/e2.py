D = int(input())
N = int(input())
mod = 10**9 + 7
from itertools import product


def count(x):
    a = str(x)
    n = len(a)
    #配列は末から
    dp=[[[0] * D for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0] = 1

    #条件に合わせてDP
    for i, less, modd in product(range(n), (0,1), range(D)):
        max_d = 9 if less else int(a[i])
        for d in range(max_d+1):
            less_ = less or d < max_d
            modd_ = (modd + d) % D
            dp[i + 1][less_][modd_] += dp[i][less][modd] % mod

    #合致するものを合算
    ret = 0
    for less in range(2):
            ret += dp[n][less][0]
    return ret

print((count(N) - count(0)) % mod)
