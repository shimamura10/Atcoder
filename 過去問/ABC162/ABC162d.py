from bisect import bisect_left
from collections import defaultdict


N = int(input())
S = input()
ans = 0
d = defaultdict(list)
for i in range(N):
    d[S[i]].append(i)
rn = len(d['R'])
gn = len(d['G']) 
bn = len(d['B'])
for i in range(N):
    s = set()
    s.add(S[i])
    for j in range(i+1,N):
        if S[j] in s:
            continue
        s.add(S[j])
        if not 'R' in s:
            ans += rn - bisect_left(d['R'],j)
            if 2*j-i < N and S[2*j-i] == 'R':
                ans -= 1
        if not 'G' in s:
            ans += gn - bisect_left(d['G'],j)
            if 2*j-i < N and S[2*j-i] == 'G':
                ans -= 1
        if not 'B' in s:
            ans += bn - bisect_left(d['B'],j)
            if 2*j-i < N and S[2*j-i] == 'B':
                ans -= 1
        s.discard(S[j])
    s.discard(S[i])
print(ans)

        