N = int(input())
A,B = [],[]
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N%2 == 1:
    md = N//2
    ansM = B[md]
    ansm = A[md]
    ans = ansM - ansm + 1
else:
    md1 = N//2 - 1
    md2 = N//2
    ansm1 = A[md1]
    ansm2 = A[md2]
    ansM1 = B[md1]
    ansM2 = B[md2]
    ans = (ansM1+ansM2)-(ansm1+ansm2)+1
print(ans)