N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A_ind = [[] for _ in range(5001)]
B_ind = [[] for _ in range(5001)]
for i in range(N):
    A_ind[A[i]].append(i)
    B_ind[B[i]].append(i)

ans = True
for i in range(5001):
    if len(A_ind[i]) != len(B_ind[i]):
        ans = False
        break
p = B[-2]
q = B[-1]
pind = A_ind[p][-1]
qind = A_ind[q][-1]
if ans:
    if pind > qind:
        ans = False
    for i in range(N):
        if p <= i+1 and q <= i+1:
            if (A_ind[B[i]] - i)%2 == 1:
                
