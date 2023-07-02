from collections import defaultdict
from email.policy import default

N = int(input())
A = list(map(int,input().split()))
d = defaultdict(int)
for a in A:
    d[a] += 1
M = 0
for v in d.values():
    M += v*(v-1)//2
for a in A:
    v = d[a]
    print(M-v+1)