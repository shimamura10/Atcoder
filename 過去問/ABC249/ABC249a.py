a,b,c,d,e,f,x = map(int,input().split())
def fun(a,b,c,x):
    ret = 0
    while True:
        if x >= a:
            ret += a*b
            x -= a
        else:
            ret += b*x
            x = 0
        x -= c
        if x <= 0:
            break
    return ret
t = fun(a,b,c,x)
aoki = fun(d,e,f,x)
if t > aoki:
    print('Takahashi')
elif t < aoki:
    print('Aoki')
else:
    print('Draw')


