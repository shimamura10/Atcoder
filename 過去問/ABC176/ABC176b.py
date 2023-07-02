n = input()
ans = 0
for i in n:
    ans += int(i)
if ans % 9 == 0:
    print('Yes')
else:
    print('No')