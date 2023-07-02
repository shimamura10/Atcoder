N,D = map(int,input().split())
ans = 0
mod = 998244353
p = [1]
for _ in range(D):
    p.append(p[-1]*2%mod)
for i in range(N):
    b = min(D-1,i)
    a = max(D-(i+1),0)
    ans *= 2
    if a <= b and D >= 2:
        ans += (b-a)*p[D-2]
    if D <= i:
        ans += p[D]
    ans %= mod
print(ans*2%mod)