S = input()
ans = 0
for i in range(3):
    if S[i] == 'R':
        ans += 1
if ans == 2 and S[1] == 'S':
    ans -= 1
print(ans)