from itertools import combinations
# print(list(permutations(range(3))))

H,W,K = map(int,input().split())
C = [input() for _ in range(H)]
max = 0
I = [0]*H
J = [0]*W
for i in range(H):
    for j in range(W):
        if C[i][j] == '#':
            max += 1
            I[i] += 1
            J [j] += 1
gyou = []
for i in range(H):
    gyou.extend(list(combinations(range(H),i+1)))
retsu = []
for i in range(W):
    retsu.extend(list(combinations(range(W),i+1)))
ans = 0
for i in gyou:
    for j in retsu:
        d = 0
        for k in i:
            d += I[k]
        for k in j:
            d += J[k]
        for k in i:
            for l in j:
                if C[k][l] == '#':
                    d -= 1
        if max - d == K:
            ans += 1
            # print(i,j)
for i in gyou:
    d = 0
    for k in i:
        d += I[k]
    if max - d == K:
        ans += 1
        # print(i)
for j in retsu:
    d = 0
    for k in j:
        d += J[k]
    if max - d == K:
        ans += 1
        # print(j)
if max == K:
    ans += 1
print(ans)
