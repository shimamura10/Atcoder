N,K,M = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)
ans = M*N - s
if ans > K:
    print(-1)
elif ans < 0:
    print(0)
else:
    print(ans)