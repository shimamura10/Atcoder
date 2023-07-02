N,K = map(int,input().split())
mod = 998244353
seen = [0]*N
for _ in range(K):
    c,k = input().split()
    k = int(k)
    k -= 1
    seen[k] = -1
    if c == 'R':
        for i in range(k):
            if seen[i] == -1:
                continue
            seen[i] += 1
    else:
        for i in range(k+1,N):
            if seen[i] == -1:
                continue
            seen[i] += 1
ans = 1
for s in seen:
    if s == -1:
        continue
    ans *= s
    ans %= mod
print(ans)