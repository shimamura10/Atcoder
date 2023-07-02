H,A = map(int,input().split())
print(H//A + (H%A and 1))
print((H+A-1)//A)