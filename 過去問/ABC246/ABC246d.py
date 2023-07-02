N = int(input())
if N**(1/3) == N:
    print(N)
    exit()
def f(a,b):
    return a**3 + a**2*b + a*b**2 + b**3
ans = float('inf')
def binary_search(function,no,ok):  #mが条件を満たすかどうかを返す関数function
    while True:                     #条件を満たさない値no
        m = (no + ok)//2            #条件を満たす値ok
        if function(m):             #ギリギリ条件を満たすindexを返す
            ok = m
        else:
            no = m
        if abs(ok - no) == 1:
            return ok
def function(m):
    if f(a,m) >= N:
        return True
    else:
        return False
for a in range(10**6):
    b = binary_search(function,0,10**6)
    ans = min(ans,f(a,b))
    # for b in range(a,10**6):
    #     x = f(a,b)
    #     if x >= N:
    #         ans = min(ans,x)
    #         break
print(ans)