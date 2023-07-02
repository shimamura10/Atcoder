a,b = input().split()
A = 0
B = 0
for i in a:
    A += int(i)
for i in b:
    B += int(i)
print(max(A,B))