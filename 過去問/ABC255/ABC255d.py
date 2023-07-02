from bisect import bisect_left
from itertools import accumulate


N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
S = list(accumulate(A))
S = [0] + S
for i in range(Q):
    x = int(input())
    idx = bisect_left(A,x)
    ans = x*idx - S[idx] + S[-1] - S[idx] - x*(N-idx)
    print(ans)
