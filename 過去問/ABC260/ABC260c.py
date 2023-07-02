N,X,Y = map(int,input().split())
red = 1
blue = 0
while N >= 2:
    blue += red*X
    red += blue
    blue *= Y
    N -= 1
print(blue)