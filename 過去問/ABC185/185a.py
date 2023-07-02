A = list(map(int,input().split()))
ans = A[0]
for i in range(4):
    if A[i] < ans:
        ans = A[i]
print(ans)

