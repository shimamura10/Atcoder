from collections import defaultdict


H,W,K = map(int,input().split())
S = [input() for _ in range(H)]
inf = float('inf')
ans = inf
for bit in range(1<<(H-1)):
    a = []
    for i in range(H-1):
        if bit >> i & 1:
            a.append(i)
    tans = len(a)
    a.append(H-1)
    tmp = defaultdict(int)
    for j in range(W):
        t = 0
        s = 0
        for i in range(H):
            s += int(S[i][j])
            if i == a[t]:
                tmp[t] += s
                s = 0
                t += 1
        # tmp[t] += s
        ok = True
        for v in tmp.values():
            if v > K:
                ok = False
                break
        if not ok:
            tans += 1
            for key in tmp:
                tmp[key] = 0
            s = 0
            t = 0
            for i in range(H):
                s += int(S[i][j])
                if i == a[t]:
                    tmp[t] += s
                    s = 0
                    t += 1
            # tmp[t] += s
            ok = True
            for v in tmp.values():
                if v > K:
                    ok = False
                    break
        if not ok:
            tans = inf
            break
    ans = min(ans,tans)
print(ans)

            
        

    