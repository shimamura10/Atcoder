from itertools import accumulate


N,K = map(int,input().split())
ans = 0

p = 10**9 + 7
s = list(accumulate(range(N+1)))
s = [0] + s
for i in range(K,N+2):
    ans = (ans+s[-1]-s[-i-1]-s[i]+1)%p
print(ans)

