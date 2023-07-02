N,K = map(int,input().split())
seen = [-1]*10**5
x = N
a = []
for i in range(K+1):
    if seen[x] == -1:
        seen[x] = i
        a.append(x)
        y = 0
        for j in range(5):
            y += (x%(10**(j+1)) - x%(10**j))//(10**j)
        x = (x+y)%(10**5)
    else:
        l = seen[x]
        r = i
        break
    if i == K-1:
        print(x)
        exit()
n = r - l
K -= l
b = K%n
print(a[l+b])

