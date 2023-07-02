N,X = map(int,input().split())
S = input()
s = []
for i in range(N):
    if S[i] == 'U':
        if len(s) == 0 or s[-1] == 'U':
            s.append('U')
        else:
            del s[-1]
    elif S[i] == 'R':
        s.append('R')
    elif S[i] == 'L':
        s.append('L')
for i in s:
    if i == 'L':
        X *= 2
    elif i == 'R':
        X = 2*X + 1
    else:
        X //= 2
print(X)