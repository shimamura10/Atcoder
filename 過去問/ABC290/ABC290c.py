N,K = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
ans = -1
for a in A:
    if a == ans +1 and K > 0:
        ans += 1
        K -= 1
print(ans+1)