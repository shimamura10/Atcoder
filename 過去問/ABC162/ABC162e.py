N,K = map(int,input().split())
mod = 10**9 + 7
ans = 0
cnt = [0]*(1+K)
for i in reversed(range(1,K+1)):
    tmp = pow(K//i,N,mod)
    for j in range(2,K//i+1):
        tmp = (tmp-cnt[i*j])%mod
    cnt[i] = tmp
for i in range(1,K+1):
    ans = (ans+cnt[i]*i)%mod
print(ans)
