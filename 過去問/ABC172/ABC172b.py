S = input()
T = input()
ans = 0
N = len(S)
for i in range(N):
    if S[i] != T[i]:
        ans += 1
print(ans)