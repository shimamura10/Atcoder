N,M = map(int,input().split())
A = list(map(int,input().split()))
dp = [[0,0]]*N
ans = 0
s = 0
for i,a in enumerate(A[:M]):
    ans += a*(i+1)
    s += a
tmp = ans
seen = [True]*M + [False]*(N-M)
for i in range(M,N):
    tmp += M*A[i]
    tmps = s
    tmptmp = 0
    cnt = 0
    for j in range(i):
        if seen[j]:
            tmptmptmp = tmp - tmps - A[j]*cnt
            tmps -= A[j]
            cnt += 1
            tmptmp = max(tmptmp,tmptmptmp)
    if tmp > ans:
        s = tmps
        ans = tmp
        seen[i] = True
        seen[] = False
