X = int(input())
ans = 1
x = 100
while True:
    x += x//100
    if x >= X:
        print(ans)
        break
    ans += 1