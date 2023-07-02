from collections import deque
from heapq import heappop, heappush


N,L = map(int,input().split())
K = int(input())
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
    cnt = 0
    l = 0
    for i in range(N):
        if A[i] - l >= x:
            cnt += 1
            l = A[i]
            if cnt == K and L-l >= x:
                return True
    return False
ans = binary_search(f,L,0)
print(ans)

