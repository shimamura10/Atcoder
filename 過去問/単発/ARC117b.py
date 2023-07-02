N = int(input())
A = list(map(int,input().split()))
A.append(0)
A.sort()
ans = 1
mod = 10**9+7
for i in range(N):
    ans *= A[i+1]-A[i]+1
    ans %= mod
print(ans)