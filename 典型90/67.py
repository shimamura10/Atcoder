N,K = input().split()
K = int(K)
n = []
for i in range(len(N)):
    n.append(int(N[-(i+1)]))
def f(n):
    num = 0
    for i in range(len(n)):
        num += n[i]*8**i
    res = []
    while num > 0:
        a = num % 9
        if a == 8:
            a = 5
        res.append(a)
        num //= 9
    return res

for _ in range(K):
    n = f(n)
ans = []
ok = False
k = 0
for i in range(len(n)):
    if n[-(i+1)] != 0:
        ok = True
    if ok:
        ans.append(n[-(i+1)])
        k += 1
a = 0
for i in range(len(ans)):
    a += ans[-(i+1)]*10**i
print(a)
