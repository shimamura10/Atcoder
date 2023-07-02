N = int(input())
a = list(map(int,input().split()))
a.sort()
ans = 0
pre = 0
for i in range(N):
    if pre != a[i]:
        ans += 1
        pre = a[i]
print(ans)