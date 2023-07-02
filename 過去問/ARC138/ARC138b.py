N = int(input())
A = list(map(int,input().split()))
if A[0] == 1:
    print('No')
    exit()
if sum(A) == 1 and A[-1] == 1:
    print('No')
    exit()
if sum(A) == 0:
    print('Yes')
    exit()
# if N == 1:
#     if A[0] == 0:
#         print('Yes')
#     else:
#         print('No')
# # elif N == 2:
# #     print('Yes')
# else:
#     if A[1] == 0:
#         print('No')
#     else:
#         print('Yes')
a = 0
b = 0
for i in range(N):
    if a % 2:
        if A[-(1+b)] == 1:
            b += 1
        else:
            if A[a] == 0:
                print('No')
                exit()
            a += 1
    else:
        if A[-(1+b)] == 0:
            b += 1
        else:
            if A[a] == 1:
                print('No')
                exit()
            a += 1
print('Yes')