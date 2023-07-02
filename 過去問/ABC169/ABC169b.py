N = int(input())
A = list(map(int,input().split()))
A.sort()
k = 10**18
ans = 1
for a in A:
    ans *= a
    if ans > k:
        ans = -1
        break
print(ans)