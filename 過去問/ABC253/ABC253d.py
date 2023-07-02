from math import gcd


N,A,B = map(int,input().split())
ans = N*(1+N)//2
a = (N//A)*(A+A*(N//A))//2
b = (N//B)*(B+B*(N//B))//2
AB = A*B//gcd(A,B)
ab = (N//(AB))*(AB+AB*(N//AB))//2
print(ans-a-b+ab)