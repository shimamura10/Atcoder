S = input()
T = input()
s = len(S)
t = len(T)
ans = t
for i in range(s-t+1):
    tmp = 0
    for j in range(t):
        if S[i+j] != T[j]:
            tmp += 1
    ans = min(ans,tmp)
print(ans)