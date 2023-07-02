N,K = map(int,input().split())
c = [0]*(N+1)
for i in range(2,N+1):
    if c[i] != 0:
        continue
    j = 1
    while i*j <= N:
        c[i*j] += 1
        j += 1
ans = 0
for i in range(N+1):
    if c[i] >= K:
        ans += 1
print(ans)