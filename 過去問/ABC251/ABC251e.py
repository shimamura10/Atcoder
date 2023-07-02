N = int(input())
A = list(map(int,input().split()))
Asort = [(A[i],i) for i in range(N)]
Asort.sort()
seen = [2]*N
ans = sum(A)
for a,i in Asort[::-1]:
    if seen[i] == 1 or seen[(i+1)%N] == 1:
        continue
    ans -= a
    seen[i] -= 1
    seen[(i+1)%N] -= 1

# seen = [False]*N
# ans = 0
# for a,i in Asort:
#     if seen[i] or seen[(i+1)%N]:
#         continue
#     ans += a
#     seen[i] = True
#     seen[(i+1)%N] = True
# for i in range(N):
#     if seen[i]:
#         continue
#     a = A[i]
#     b = A[i-1]
#     if a < b:
#         seen[i] = True
#         seen[i+1] = True
#         ans += a
#     elif b <= a:
#         seen[i] = True
#         seen[i-1] = True
#         ans += b
# if sum(seen) == 0:
#     print(A[0]*(N+1)//2)
#     exit()
# ini = -1
# for i in range(N):
#     if seen[i]:
#         ini = i
# for i in range(ini,N+ini):
#     i %= N
#     if seen[i]:
#         continue
#     ans += A[i]
#     seen[i] = True
#     seen[(i+1)%N] = True
print(ans)