
from itertools import product

a = int(input())
K = int(input())

def count(x):
    a = str(x)
    n = len(a)
    #配列は末から
    dp=[[[0] * (K+1) for _ in range(2)] for _ in range(n+1)]
    dp[0][0][0] = 1

    #条件に合わせてDP
    for i, less, hasno0 in product(range(n), (0,1), range(K+1)):
        max_d = 9 if less else int(a[i])
        for d in range(max_d+1):
            less_ = less or d < max_d
            if d > 0:
                hasno0_ = hasno0 + 1
            else:
                hasno0_ = hasno0
            if hasno0_ > K:
                continue
            dp[i + 1][less_][hasno0_] += dp[i][less][hasno0]

    #合致するものを合算
    ret = 0
    for less in range(2):
            ret += dp[n][less][K]
    return ret
print(count(a))