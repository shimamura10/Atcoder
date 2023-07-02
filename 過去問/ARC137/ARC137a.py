from math import gcd

L,R = map(int,input().split())
ans = 0
l = L
r = R
while True:
    if gcd(l,r) == 1:
        break
    r -= 1
ans = r - l
for i in range(L+1,L+R-r+1):
    r = R
    while True:
        if gcd(i,r) == 1:
            break
        r -= 1
    ans = max(ans,r-i)
print(ans)
