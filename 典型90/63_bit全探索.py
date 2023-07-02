H,W = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(H)]
a = list(range(H))
b = []
for bit in range(1<<H):
    s = []
    for j in range(H):
        if bit & 1<<j:
            s.append(a[j])
    if s == []:
        continue
    b.append(s)
ans = 0
for i in b:
    num = [0]*(1+H*W)
    for j in range(W):
        ok = True
        for k in range(len(i)-1):
            if P[i[k]][j] != P[i[k+1]][j]:
                ok = False
                break
        if ok:
            num[P[i[0]][j]] += 1
    ans = max(ans,max(num)*len(i))
print(ans)