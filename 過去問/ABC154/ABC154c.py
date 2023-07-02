N = int(input())
A = list(map(int,input().split()))
s = set()
for a in A:
    if a in s:
        print('NO')
        exit()
    s.add(a)
print('YES')