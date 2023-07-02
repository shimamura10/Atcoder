from math import factorial


A,B,K = map(int,input().split())
S = factorial(A+B)//factorial(A)//factorial(B)
ans = []
min = 0
for i in range(A+B):
    s = factorial(A+B-1)//factorial(A-1)//factorial(B)
    if min + s >= K:
        ans.append('a')
        A -= 1
        if A == 0:
            ans += ['b']*B
            break
    else:
        ans.append('b')
        B -= 1
        min += s
        if B == 0:
            ans += ['a']*A
            break
print(''.join(ans))

a = 5
for i in range(a):
    a -= 1
    print(i)