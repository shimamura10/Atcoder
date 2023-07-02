N = int(input())
A = list(map(int,input().split()))
ans = 0
L = [N]*N
n = []
pa = 0
for i in range(N):
    if pa > A[i]:       
        while A[i] < A[n[-1]]:
            L[n[-1]] = i
            del n[-1]
            if len(n) == 0:
                break
    n.append(i)
    pa = A[i]
    # print(i,n,L)
B = A[::-1]
R = [N]*N
pb = 0
nb = []
for i in range(N):
    if pb > B[i]:       
        while B[i] < B[nb[-1]]:
            R[nb[-1]] = i
            del nb[-1]
            if len(nb) == 0:
                break
    nb.append(i)
    pb = B[i]
    # print(i,nb,R)
# while len(n) != 0:
#     L[n[-1]] = N
#     del n[-1]

for i in range(N):
    sl = A[i]*(L[i]-i)
    # sl = A[i]*(L[i]+R[N-1-i]-N)
    j = N-1-i
    sr = B[j]*(R[j]-j)
    ans = max(ans,sl+sr-A[i])
    

print(ans)
