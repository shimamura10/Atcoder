from math import gcd


a,b = list(map(int,input().split()))
print(a*b//gcd(a,b))