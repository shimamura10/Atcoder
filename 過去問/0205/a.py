n = int(input())
if n>10:
    print("Yes")
else:
    if 2**n > n**2:
        print("Yes")
    else:
        print("No")