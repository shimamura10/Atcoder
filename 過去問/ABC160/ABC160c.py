K,N = map(int,input().split())
A = list(map(int,input().split()))
A
b = K + A[0] - A[-1]
for i in range(N-1):
    b = max(b,A[i+1]-A[i])
print(K-b)