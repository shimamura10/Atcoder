N,K = map(int,input().split())
A = list(map(int,input().split()))
def binary_search(function,no,ok):  #mが条件を満たすかどうかを返す関数function
    while True:                     #条件を満たさない値no
        m = (no + ok)//2            #条件を満たす値ok
        if function(m):             #ギリギリ条件を満たさないindexを返す
            ok = m
        else:
            no = m
        if abs(ok - no) == 1:
            return ok
def f(x):
    if x == 0:
        return False
    cnt = 0
    for a in A:
        cnt += a//x
        if a%x == 0:
            cnt -= 1
    if cnt <= K:
        return True
    else:
        return False
print(binary_search(f,0,max(A)))