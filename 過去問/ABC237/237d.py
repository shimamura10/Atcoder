# a = [0,1,2,3,4,5]
# print(a[:0])
# print(a[3:])
# print(a + [1])
n = int(input())
s = input()
a = [0]
pos = 0
d = 0
l = 0
for i in range(n):
    if s[i] == "R":
        if d==1:
            a = a[:pos] + list(range(i,i-l,-1)) + a[pos:]
            l = 1
        if d==0:
            l += 1
        d = 0
    if s[i] == "L":
        if d==0:
            a = a[:pos+1] + list(range(i-l+1,i+1)) + a[pos+1:]
            pos += l
            l = 1
        if d==1:
            l += 1
        d = 1
if d==1:
    a = a[:pos] + list(range(n,n-l,-1)) + a[pos:]
if d==0:
    a = a[:pos+1] + list(range(n-l+1,n+1)) + a[pos+1:]

print(*a)
# b = list(range(7,7,-1))
# print(b)