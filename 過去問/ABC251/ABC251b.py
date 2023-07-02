N,W = map(int,input().split())
A = list(map(int,input().split()))
ans = [0]*(W+1)
for i in range(N):
    a = A[i]
    if a <= W:
        ans[a] = 1
    for j in range(i):
        a = A[i] + A[j]
        if a <= W:
            ans[a] = 1
        for k in range(j):
            a = A[i] + A[j] + A[k]
            if a <= W:
                ans[a] = 1
print(sum(ans))