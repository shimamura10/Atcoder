N,Q = map(int,input().split())
A = list(map(int,input().split()))
dis = []
ans = 0
for i in range(N-1):
    dis.append(A[i+1]-A[i])
    ans += abs(A[i+1]-A[i])
for i in range(Q):
    l,r,v = map(int,input().split())
    l -= 1
    r -= 1
    if l > 0:
        tmp = dis[l-1]
        dis[l-1] += v
        ans += abs(dis[l-1]) - abs(tmp)
    if r < N - 1:
        tmp = dis[r]
        dis[r] -= v
        ans += abs(dis[r]) - abs(tmp)
    print(ans)