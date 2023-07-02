N = int(input())
A = list(map(int,input().split()))
max = 0
for i in range(2**N):
    if A[max] < A[i]:
        max = i
if max < 2**(N-1):
    ans = 2**(N-1)
    for i in range(2**(N-1),2**N):
        if A[ans] < A[i]:
            ans = i
else:
    ans = 0
    for i in range(2**(N-1)):
        if A[ans] < A[i]:
            ans = i

print(ans+1)
