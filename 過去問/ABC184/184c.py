r1,c1 = map(int,input().split())
r2,c2 = map(int,input().split())
ans = 3
if r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2 or abs(r1-r2) + abs(c1-c2) <= 3:
    ans = 1
else:
    x = r2 - r1
    y = c2 - c1
    if abs(x-y) <= 3 or abs(x+y) <= 3:
        ans = 2
    if (x-y)%2 == 0:
        ans = 2
    for a in range(-3,4):
        for b in range(-(3-abs(a)),4-abs(a)):
            if a + b == x + y or a - b == x - y or abs(a-x) + abs(b-y) <= 3:
                ans = 2
if r1 == r2 and c1 == c2:
    ans = 0
print(ans)
    