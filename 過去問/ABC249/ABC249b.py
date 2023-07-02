S = input()
seen = set()
big = False
sm = False
di = True
for s in S:
    n = ord(s)
    if ord('a') <= n and n <= ord('z'):
        sm = True
    if ord('A') <= n and n <= ord('Z'):
        big = True
    if n in seen:
        di = False
    seen.add(n)
if big and sm and di:
    print('Yes')
else:
    print('No')