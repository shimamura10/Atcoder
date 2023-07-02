from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = [defaultdict(int) for _ in range(N)]
for i in range(N):
    for j in range(N):
        cnt[i][A[i]^B[j]] += 1
ans = []
for x in cnt[0].keys():
    cntb = defaultdict(int)
    ok = True
    for i in range(N):
        b = A[i]^x
        if cnt[i][x] - cntb[b] <= 0:
            ok = False
            break
        cntb[b] += 1
    if ok:
        ans.append(x)
ans.sort()
print(len(ans))
for a in ans:
    print(a)