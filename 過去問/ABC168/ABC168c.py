from math import cos, pi, sin, sqrt


A,B,C,D = map(int,input().split())
the = (C/12+D/720-D/60)*2*pi
print(sqrt(A**2+B**2-2*A*B*cos(the)))