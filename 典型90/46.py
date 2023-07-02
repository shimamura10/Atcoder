N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
na = [0]*46
nb = [0]*46
nc = [0]*46
for i in range(N):
    na[a[i]%46] += 1
    nb[b[i]%46] += 1
    nc[c[i]%46] += 1
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k)%46 == 0:
                ans += na[i]*nb[j]*nc[k]
print(ans)