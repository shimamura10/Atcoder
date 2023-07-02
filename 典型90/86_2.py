N,Q = map(int,input().split())
query = []
for _ in range(Q):
    x,y,z,w = map(int,input().split())
    x -= 1
    y -= 1
    z -= 1
    query.append([x,y,z,w])
ans = 1
mod = 10**9+7
for i in range(60):
    tmp = 0
    for bit in range(1<<N):
        ok = True
        for j in range(Q):
            x,y,z,w = query[j]
            if (bit>>x & 1) | (bit>>y & 1) | (bit>>z & 1) != w>>i & 1:
                ok = False
                break
        if ok:
            tmp += 1
    ans *= tmp
    ans %= mod
print(ans)