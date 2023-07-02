from bisect import bisect_left, bisect_right
from itertools import accumulate

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
A = [0] + A
B = list(map(int,input().split()))
sumA = list(accumulate(A))
sumB = list(accumulate(B))
ans = 0
for i in range(N+1):
    if sumA[i] > K:
        break
    j = bisect_right(sumB,K-sumA[i])
    ans = max(ans,i+j)

print(ans)
