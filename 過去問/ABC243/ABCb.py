N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = 0
b = 0
for i in range(N):
    for j in range(N):
        if i == j and A[i] == B[j]:
            a += 1
        else:
            if A[i] == B[j]:
                b += 1
print(a)
print(b)