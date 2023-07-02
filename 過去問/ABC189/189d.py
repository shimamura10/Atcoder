N = int(input())
s = input()
if s == 'OR':
    ans = 3
else:
    ans = 1
for i in range(N-1):
    s = input()
    if s == 'OR':
        ans += 2**(i+2)
print(ans)