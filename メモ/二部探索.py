#ある境目で条件を満たす満たさないが変わるときの境目を探す
from bisect import bisect_left, bisect_right


l = [1,2,4,4,6,7,7,9]
#k以上の値のうち最小のもののindexを求める
no = -1
ok = len(l)
k = 4
while True:
    m = (no + ok)//2
    if l[m] >= k:
        ok = m
    else:
        no = m
    if abs(ok - no) == 1:
        break
print(no,ok)   #1 2
print(bisect_left(l,k)) #2

#kより大きい値のうち最小のもののindexを求める
ok = len(l)
no = -1
k = 4
while True:
    m = (no + ok)//2
    if l[m] > k:
        ok = m
    else:
        no = m
    if abs(ok - no) == 1:
        break
print(ok,no)  #4 3
print(bisect_right(l,k))  #4

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
    if l[x] > k:
        return True
    else:
        return False
print(binary_search(f,-1,len(l)))  #4

https://www.forcia.com/blog/001434.html