from bisect import bisect_left, bisect_right
from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
Q = int(input())
d = defaultdict(list)
for i,a in enumerate(A):
    d[a].append(i)
for _ in range(Q):
    l,r,x = map(int,input().split())
    l -= 1
    r -= 1
    m = bisect_left(d[x],l)
    M = bisect_right(d[x],r)
    print(M-m)
    