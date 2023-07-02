from collections import defaultdict


S = input()
N = len(S)
mod = 2019
p = [1]
for i in range(N):
    p.append(p[-1]*10%mod)
cnt = defaultdict(int)
cnt[0] = 1
ans = 0
x = 0
for i in reversed(range(N)):
    x = (x+int(S[i])*p[N-1-i])%mod
    ans += cnt[x]
    cnt[x] += 1
print(ans)