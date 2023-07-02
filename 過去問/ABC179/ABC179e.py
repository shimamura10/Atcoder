N,X,M = map(int,input().split())
seen = [-1]*M
sum = [0]*(M+1)
# l,r = 0,0
for i in range(N):
    if seen[X] == -1:
        seen[X] = i
        sum[i+1] = sum[i] + X
        X = X**2%M
    else:
        l = seen[X]
        r = i
        break
    if i == N-1:
        print(sum[N])
        exit()
ans = 0
ans += sum[l]
N -= l
s = sum[r] - sum[l]
ans += s*(N//(r-l))
q = N%(r-l)
ans += sum[l+q] - sum[l]
print(ans)

