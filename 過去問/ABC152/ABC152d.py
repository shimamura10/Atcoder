N = int(input())
ans = 0
n = str(N)
if len(n) == 1:
    print(N)
    exit()
elif len(n) == 2:
    for a in range(N+1):
        A = str(a)
        if A[-1] == '0':
            continue
        if A[0] == A[-1]:
            ans += 1
        if int(A[-1]+A[0]) <= N:
            ans += 1 
else:
    midn = ''
    for i in range(len(n)-2):
        midn += n[i+1]
    midn = int(midn) + 1
    for a in range(N+1):
        A = str(a)
        if A[-1] == '0':
            continue
        if A[0] == A[-1]:
            ans += 1
        if int(A[-1]+A[0]) <= N:
            ans += 1 
        for i in range(len(n)-3):
            ans += 10**(i+1)
        if int(A[-1]) < int(n[0]):
            ans += 10**(len(n)-2)
        elif A[-1] == n[0]:
            ans += midn
            if int(A[0]) > int(n[-1]):
                ans -= 1
print(ans)
# for a in range(10**(len(n)-1)):
#     A = str(a)
#     if A[-1] == '0':
#         continue

#     if len(A) == len(n):
#         if int(A[-1]) > int(n[0]):
#             continue
#         if len(A) <= 2:
#             ans += 1
#             continue
#         if int(A[-1]) < int(n[0]):
#             ans += 10**(len(A)-2)
#         elif int(A[-1]) == int(n[0]):
#             tmp = ''
#             for i in range(max(0,len(n)-2)):
#                 tmp += N[i+1]
#             tmp = int(tmp)
#             if int(A[0]) > int(n[-1]):
#                 tmp -= 1
#             ans += tmp
#     elif len(A) <= 2:
#         ans += 1
#     else:
#         ans += 10**(len(A)-2)
# print(ans)


# for a in range(1,N+1):
#     A = str(a)
#     if A[-1] == '0':
#         continue
#     ans += (len(A)-2,)
#     if len(A) == len(n):
#         if int(A[-1]) < int(n[0]):
#             ans += 10**(len(A)-2)
#         elif int(A[-1]) == int(n[0]):
#             tmp = ''
#             for i in range(max(0,len(n)-2)):
#                 tmp += N[i+1]
#             if int(A[0]) > int(n[-1]):

