from math import gcd


def inv_gcd(a,b):
    a=a%b
    if a==0:
        return (b,0)
    s=b;t=a
    m0=0;m1=1
    while(t):
        u=s//t
        s-=t*u
        m0-=m1*u
        s,t=t,s
        m0,m1=m1,m0
    if m0<0:
        m0+=b//s
    return (s,m0)
def inv_mod(x,m):
    assert 1<=m
    z=inv_gcd(x,m)
    assert z[0]==1
    return z[1]
def crt(r,m,M):
    assert len(r)==len(m)
    n=len(r)
    r0=0;m0=1
    for i in range(n):
        assert 1<=m[i]
        r1=r[i]%m[i]
        m1=m[i]
        if m0<m1:
            r0,r1=r1,r0
            m0,m1=m1,m0
        if (m0%m1==0):
            if (r0%m1!=r1):
                return (0,0)
            continue
        g,im=inv_gcd(m0,m1)
        u1=m1//g
        if ((r1-r0)%g):
            return (0,0)
        x=(r1-r0)//g % u1*im%u1
        r0+=x*m0
        m0*=u1
        if r0<0:
            r0+=m0
        if r0 > M:
            return r0,0
    return (r0,m0)

def floor_sum(n,m,a,b):
    ans=0
    if a>=m:
        ans+=(n-1)*n*(a//m)//2
        a%=m
    if b>=m:
        ans+=n*(b//m)
        b%=m
    y_max=(a*n+b)//m
    x_max=(y_max*m-b)
    if y_max==0:
        return ans
    ans+=(n-(x_max+a-1)//a)*y_max
    ans+=floor_sum(y_max,a,m,(a-x_max%a)%a)
    return ans

#ACL部分は省略
# #3で割ると2余り、5で割ると3余り、7で割ると2余る
# C = [3,5,7]#これで割ったら
# R = [2,3,2]#この余りになる対のリスト
# r,m = crt(R,C)
# print(r)#23

#返り値の二つ目が0なら条件が矛盾している。

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = [a//2 for a in A]
r,m = crt(B,A,M)
a = A[0]
g = 1
ok = True
for i in range(N-1):
    g = gcd(a,A[i+1])
    a = a//g*A[i+1]
    if a > M:
        ok = False
        break
if m == 0:
    print(0)
    exit()
print((M-r)//a+1)