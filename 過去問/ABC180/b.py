N = int(input())
x = list(map(int,input().split()))
a,b,c = 0,0,0
for i in range(N):
    a += abs(x[i])
    b += x[i]*x[i]
    c = max(c,abs(x[i]))
print(a)
print(b**0.5)
print(c)