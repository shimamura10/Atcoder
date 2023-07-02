s = input()
ABC = ['A','B','C']
# print(ABC.index('B'))
q = int(input())
# def pow(x, n, k):
#     ans = 1
#     # // n が 0 になるまで計算を続ける
#     while n:
#         if n % 2:
#             ans *= x
#         x *= x
#         n >>= 1
#         if ans > k:
#             ans = k+1
#             break
#     return ans

def pow(x, n, k):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
        if K*x > k:
            break

    return K * x
for i in range(q):
    t,k = map(int,input().split())
    c = pow(2,t,k)
    if c > k:
        a = 0
    elif k%c == 0:
        a = k//c - 1
    else:
        a = k//c
    k -= 1
    b = 0
    n = 0
    d = k % c
    while d > 0 and n < t:
        if d%2 == 0:
            b += 1
        else:
            b -= 1
        d //= 2
        n += 1
    # if d%2 == 0:
    #     b += 1
    # else:
    #     b -= 1
    # print(a,b,n)
    if (t-n)%3 == 0:
        print(ABC[(ABC.index(s[a])+b)%3])
    if (t-n)%3 == 1:
        print(ABC[(ABC.index(s[a])+1+b)%3])
    if (t-n)%3 == 2:
        print(ABC[(ABC.index(s[a])+2+b)%3])
    