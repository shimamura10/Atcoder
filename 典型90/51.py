from bisect import bisect_left, bisect_right
from collections import deque
from itertools import combinations
# print(list(combinations(range(1),1)))
 
N,K,P = map(int,input().split())
A = list(map(int,input().split()))
A1 = A[:N//2]
# A1.sort()
A2 = A[N//2:]
# A2.sort()
n1 = len(A1)
n2 = len(A2)
g1 = [[0]]
g2 = [[0]]
for i in range(n1):
    res = []
    for j in combinations(range(n1),i+1):
        sum = 0
        for k in j:
            sum += A1[k]
        res.append(sum)
    res.sort()
    g1.append(res)
for i in range(n2):
    res = []
    for j in combinations(range(n2),i+1):
        sum = 0
        for k in j:
            sum += A2[k]
        res.append(sum)
    res.sort()
    g2.append(res)
# print(g1)
# print(g2)
ans = 0
for i in range(len(g1)):
    if 0 > K-i or K-i > n2:
        continue
    for j in g1[i]:
        # a = bisect_left(g2[K-i],P-g1[i][j])
        # b = bisect_right(g2[K-i],P-g1[i][j])
        ans += bisect_right(g2[K-i],P-j)
print(ans)