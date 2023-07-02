N = int(input())
S = input()
ans = 0
tmp = 1
for i in range(N-1):
    if S[i] != S[i+1]:
        ans += tmp*(1+tmp)//2
        tmp = 1
    else:
        tmp += 1
ans += tmp*(1+tmp)//2
print(N*(N+1)//2-ans)