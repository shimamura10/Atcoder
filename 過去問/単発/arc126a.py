t = int(input())
for i in range(t):
    n2,n3,n4 = map(int,input().split())
    ans = 0
    n3 //= 2
    a = min(n3,n4)
    ans += a
    n3 -= a
    n4 -= a
    if n3 > 0:
        if n3*2 > n2:
            ans += n2//2
            n2 -= n2//2*2
        else:
            ans += n3
            n2 -= n3
    if n4 > 0:
        if n4//2 > n2:
            ans += n2
            n2 -= n2
            n4 -= n2*2
        else:
            ans += n4//2
            n2 -= n4//2
            n4 -= n4//2*2
    n2 += n4*2
    ans += n2//5
    print(ans)
    # if n3//2 >= n4 + n2//2:
    #     print(n3//2)
    #     continue
    # elif n3//2 < n4:
    #     n4 -= n3//2
    #     ans = n3//2
    #     if n4//2 > n2:
    #         ans += n2
    #         print(ans)
    #         continue
    #     n2 += n4*2
    #     ans += n2//5
    #     print(ans)
    #     continue
    # else:
    #     ans = 0
    #     if n4//2 > n2:
    #         ans = n2
    #         n2 -= n4//2
    #         n4 -= n4//2
    #     n2 += n4*2
    #     ans += n3//2
    #     n2 -= n3//2*2
    #     ans += n2//5
    #     print(ans)
