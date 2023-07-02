N = int(input())
if N%2:
    print(0)
else:
    ans = 0
    p = 10
    while N >= p:
        ans += N//p
        p *= 5
    print(ans)