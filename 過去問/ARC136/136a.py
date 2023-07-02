N = int(input())
S = input()
ans = [S[0]]
for i in range(1,N):
    if S[i] == 'C':
        ans.append('C')
    if S[i] == 'B':
        if ans[-1] == 'B':
            ans[-1] = 'A'
        else:
            ans.append('B')
    if S[i] == 'A':
        if ans[-1] == 'B':
            ans[-1] = 'A'
            ans.append('B')
        else:
            ans.append('A')
print(''.join(ans))
# a = []
# if a[-1] == 0:
#     print(a)