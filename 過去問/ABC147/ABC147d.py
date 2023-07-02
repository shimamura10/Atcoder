N = int(input())
A = list(map(int,input().split()))
mod = 10**9 + 7
s = [0]*60
ans = 0
p = [1]
for _ in range(60):
    p.append(p[-1]*2%mod)
n = 0
for a in A[::-1]:
    for i in range(60):
        if a >> i & 1:
            ans += (n-s[i])*p[i]
            s[i] += 1
        else:
            ans += s[i]*p[i]
        ans %= mod
    n += 1
print(ans)