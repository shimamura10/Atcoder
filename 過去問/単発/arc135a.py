import time
X = int(input())
mod = 998244353
# dict = {}
# def f(a):
#     if not(a in dict.keys()):
#         # print(a)
#         if a>4:
#             if a%2 == 0:
#                 ans = f(a//2)**2%x
#             else:
#                 sa = a//2
#                 ba = a//2 + 1
#                 ans = f(sa)*f(ba)%x
#         else:
#             ans = a
#         dict[a] = ans
#         return ans
#     else:
#         return dict[a]
# print(f(X)%998244353)
# print(dict)
n = 1
# c = 0
def pow_k(x,n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if n%2 == 1:
            K = K*x%mod
        x = x**2%mod
        n //= 2
        # print(time.time())
    return K * x % mod

def g(a,b,n,m):
    # global c
    # c += 1
    if b > 4:
        if a%2 == 1:
            na = a//2
            nb = a//2 + 1
            m = n + 2*m
        else:
            na = b//2
            nb = b//2 + 1
            n = 2*n + m
        return g(na,nb,n,m)
    # print('owari',time.time())
    # print(a,b,n,m)
    ans = pow_k(a,n)*pow_k(b,m)
    # print('owaowari',time.time())
    return ans

while X%2 == 0 and X>4:
    X = X//2
    n = n*2
if X%2 == 1 and X>4:
    a = X//2
    b = X//2 + 1
    ans = g(a,b,n,n)%mod
    # print('a')
else:
    ans = pow_k(X,n)%mod
print(ans)
# print(c)
