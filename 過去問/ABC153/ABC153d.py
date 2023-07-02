H = int(input())
ans = 0
n = 1
while H > 0:
    if H == 1:
        H = 0
        ans += n
    else:
        H //= 2
        ans += n
        n *= 2
print(ans)