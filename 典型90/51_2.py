from bisect import bisect_right


N,K,P = map(int,input().split())
A = list(map(int,input().split()))
A1 = A[:N//2]
A2 = A[N//2:]
def f(A):
    N = len(A)
    res = [[] for i in range(len(A)+1)]
    for a in A:
        for i in reversed(range(N+1)):
            for d in res[i]:
                res[i+1].append(d+a)
        res[1].append(a)
    for i in range(len(res)):
        res[i].sort()
    res[0].append(0)
    return res
cnt1 = f(A1)
cnt2 = f(A2)
ans = 0
for i,clis in enumerate(cnt1):
    if i > K:
        break
    for c in clis:
        if K-i >= len(cnt2):
            continue
        ans += bisect_right(cnt2[K-i],P-c)
print(ans)