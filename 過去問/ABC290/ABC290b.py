N,K = map(int,input().split())
S = input()
ans = ''
for i,s in enumerate(S):
    if K > 0 and s == 'o':
        ans += 'o'
        K -= 1
    else:
        ans += 'x'
print(ans)