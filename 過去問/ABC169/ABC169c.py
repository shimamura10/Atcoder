A,B = input().split()
A = int(A)
b1 = int(B[0])
b2 = int(B[2])
b3 = int(B[3])
ans = 0
ans += b1*A*100
ans += b2*A*10
ans += b3*A
print(ans//100)