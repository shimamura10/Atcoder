N,M = map(int,input().split())
A = []
for _ in range(M):
    c = int(input())
    A.append(list(map(int,input().split())))
ans = 0
for bit in range(1<<M):
    ok = True
    for i in range(N):
        ok2 = False
        for j in range(M):
            if bit >> j & 1:
                if i+1 in A[j]:
                    ok2 = True
        if not ok2:
            ok = False
            break
    if ok:
        ans += 1
print(ans)
