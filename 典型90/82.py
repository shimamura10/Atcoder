L,R = map(int,input().split())
mod = 10**9+7
i = 0
while 10**i-L <= 0:
    i += 1
j = 0
while 10**j-R<=0:
    j += 1
ans = 0
if i == j:
    ans += i*(R-L+1)*(R+L)//2%mod
    print(ans)
    exit()
ans += i*(10**i-L)*(10**i-1+L)//2%mod
for k in range(i,j-1):
    ans += (k+1)*9*10**k*(10**(k+1)+10**k-1)//2%mod
ans += j*(R-10**(j-1)+1)*(10**(j-1)+R)//2%mod
print(ans%mod)
