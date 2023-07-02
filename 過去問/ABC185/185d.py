N,M = map(int,input().split())
A = list(map(int,input().split()))
A.append(0)
A.sort()
A.append(N+1)
k = 10**9
b = []
for i in range(M+1):
    l = A[i+1]-A[i]-1
    b.append(l)
    if l == 0:
        continue
    k = min(k,l)
ans = 0
# i = A[0]-1
# j = N-A[-1]
# b.append(i)
# b.append(j)
for i in range(M+1):
    l = b[i]
    if l % k ==0:
        ans += l//k
    else:
        ans += l//k + 1


print(ans)


    