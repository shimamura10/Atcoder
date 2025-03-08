a = [1,4,2,5,1]
#aのi番目を末尾にもつ最長増加部分列の長さを求める。
n = []
from bisect import bisect_left
inf = float('inf')
dp = [inf]*len(a)
for i in range(len(a)):
    idx = bisect_left(dp,a[i])
    dp[idx] = a[i]
    n.append(idx+1)
    print(dp)
print(n)   #[1, 2, 2, 3, 1]