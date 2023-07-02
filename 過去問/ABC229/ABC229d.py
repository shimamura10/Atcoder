S = input()
K = int(input())
cou = []
p = 'X'
c = 0
for s in S:
    if s == p:
        c += 1
    else:
        cou.append(c)
        c = 1
        p = s
cou.append(c)
ans = 0
r = 1
now = 0
nowk = 0
for i,c in enumerate(cou):
    if i%2 == 0:
        now += c
        ans = max(ans,(now+nowk))
    else:
        nowk += c
        while nowk > K:
            if nowk - cou[r] >= K:
                nowk -= cou[r]
                now -= cou[r-1]
                r += 2
            else:
                cou[r] -= (nowk - K)
                nowk = K
                now -= cou[r-1]
                cou[r-1] = 0
        ans = max(ans,(now+nowk))
print(ans)