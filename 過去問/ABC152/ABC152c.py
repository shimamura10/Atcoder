N = int(input())
P = list(map(int,input().split()))
m = 10**9
ans = 0
for p in P:
    if m >= p:
        ans += 1
    m = min(m,p)
print(ans)