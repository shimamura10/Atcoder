from math import sqrt


A,B = map(int,input().split())
D = sqrt(A**2+B**2)
print(*[A/D,B/D])
