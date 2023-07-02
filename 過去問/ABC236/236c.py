nm = list(map(int,input().split()))
s = input().split()
t = input().split()
c = 0
for i in range(nm[0]):
    if s[i] == t[c]:
        print("Yes")
        c += 1
    else:
        print("No")
