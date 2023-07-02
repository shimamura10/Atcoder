N = int(input())
s = [input() for _ in range(N)]
simin = 200
simax = 0
sjmin = 200
sjmax = 0
for i in range(N):
    for j in range(N):
        if s[i][j] == '#':
            simin = min(simin,i)
            simax = max(simax,i)
            sjmin = min(sjmin,j)
            sjmax = max(sjmax,j)
t = [input() for _ in range(N)]
timin = 200
timax = 0
tjmin = 200
tjmax = 0
for i in range(N):
    for j in range(N):
        if t[i][j] == '#':
            timin = min(timin,i)
            timax = max(timax,i)
            tjmin = min(tjmin,j)
            tjmax = max(tjmax,j)
ans1 = False
ans2 = False
ans3 = False
ans4 = False
if simax-simin == timax-timin and sjmax-sjmin == tjmax-tjmin:
    ans1 = True
    for i in range(timin,timax+1):
        for j in range(tjmin,tjmax+1):
            if t[i][j] != s[simin+i-timin][sjmin+j-tjmin]:
                ans1 = False
    ans2 = True
    for i in range(timax,timin-1,-1):
        for j in range(tjmax,tjmin-1,-1):
            if t[i][j] != s[simin+timax-i][sjmin+tjmax-j]:
                ans2 = False

if simax-simin == tjmax-tjmin and sjmax-sjmin == timax-timin:
    ans3 = True
    for j in range(tjmax,tjmin-1,-1):
        for i in range(timin,timax+1):
            if t[i][j] != s[simin+tjmax-j][sjmin+i-timin]:
                ans3 = False
    ans4 = True
    for j in range(tjmin,timax+1):
        for i in range(timax,timin-1,-1):
            if t[i][j] != s[simin+j-tjmin][sjmin+timax-i]:
                ans4 = False
if ans1 or ans2 or ans3 or ans4:
    print('Yes')
else:
    print('No')
