N = int(input())
a = []
for i in range(N):
    b,c = map(int,input().split())
    if b == c:
        a.append(True)
    else:
        a.append(False)
for i in range(N-2):
    if a[i] and a[i+1] and a[i+2]:
        print('Yes')
        exit()
print('No')