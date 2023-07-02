import bisect
N,Q = map(int,input().split())
A = list(map(int,input().split()))
x = [int(input()) for i in range(Q)]
A.sort()
# def f(x):
#     a = 0
#     b = N - 1
#     for i in range(20):
#         k = (a+b)//2
#         if A[k] >= x:
#             b = k 
#         else:
#             a = k 
#     return k
for i in range(Q):
    print(N-bisect.bisect_left(A,x[i]))