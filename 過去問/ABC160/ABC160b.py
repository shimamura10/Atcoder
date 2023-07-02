X = int(input())
a = X//500
X %= 500
b = X//5
ans = 1000*a + 5 * b
print(ans)