from math import sqrt


A,B = map(int,input().split())
if A < B:
    A,B = B,A
if A*sqrt(3) >= 2*B:
    print(2/sqrt(3)*B)
else:
    cosinv = sqrt(((sqrt(3)-(2*A/B))**2+1))
    print(B*cosinv)