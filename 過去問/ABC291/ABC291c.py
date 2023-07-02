N = int(input())
S = input()
s = set()
s.add((0,0))
x,y = 0,0
for d in S:
    if d == 'R':
        x += 1
    elif d == 'L':
        x -= 1
    elif d == 'U':
        y += 1
    elif d == 'D':
        y -= 1
    if (x,y) in s:
        print('Yes')
        exit()
    s.add((x,y))
print('No')