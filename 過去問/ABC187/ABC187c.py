from re import L


N = int(input())
S = set()
Sa = set()
for i in range(N):
    s = input()
    if s[0] == '!':
        Sa.add(s)
    else:
        S.add(s)
for s in S:
    ns = '!' + s

    if ns in Sa:
        print(s)
        exit()
print('satisfiable')