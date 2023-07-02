s = input()
n = len(s)
for i in range(n+1):
    t = "a"*(i) + s
    c = 0
    j = 0
    while c == 0 and j < n:
        if t[j] != t[n+i-1-j]:
            c += 1
        j += 1
    if c == 0:
        print("Yes")
        break
if c != 0:
    print("No")