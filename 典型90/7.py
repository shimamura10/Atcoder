from bisect import bisect_left

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
A.sort()
for _ in range(Q):
    b = int(input())
    ind = bisect_left(A,b)
    print(min(abs(b-A[min(ind,N-1)]),abs(b-A[ind-1])))
