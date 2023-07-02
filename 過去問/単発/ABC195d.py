from bisect import bisect_left, bisect_right


N,M,Q = map(int,input().split())
VW = []
for i in range(N):
    w,v = map(int,input().split())
    VW.append((v,w))
X = list(map(int,input().split()))
VW = sorted(VW,reverse=True)
for _ in range(Q):
    l,r = map(int,input().split())
    tmpx = X[:l-1] + X[r:]
    tmpx = sorted(tmpx,reverse=True)
    tmpx.sort()
    i = 0
    ans = 0
    for v,w in VW:
        ind = bisect_left(tmpx,w)
        if ind < len(tmpx):
            ans += v
            del tmpx[ind]
    print(ans)
