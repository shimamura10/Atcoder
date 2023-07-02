N = int(input())
A = list(map(int,input().split()))
A0 = A[0]
ans = 0
d = 0
if A[-1] < A[0]:
    d = A[-1]
    ans += d
    A[0] -= d
elif A[-1] > A[0]:
    d = A[0]
    ans += d
    A[-1] -= d
    A[0] = 0
elif A[-1] == A[0]:
    d = A[0]
    ans += d
print(ans,d)
for i in range(N-1):
    if d == 0:
        d = A[i]
        ans += d
        print(d)
    elif d < A[i+1]:
        A[i+1] -= d
        A[i] = 0
        d = 0
    elif d > A[i+1]:
        ans += A[i]
        d = A[i+1]
        A[i] = 0
        A[i+1] = 0
    elif d == A[i+1]:
        A[i] = 0
        A[i+1] = 0
    print(ans,d)

# if A[-1] > A0:
#     ans += A[-1] - A0

print(ans)


