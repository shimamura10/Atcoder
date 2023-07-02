H,W,K = map(int,input().split())
sx,sy,gx,gy = map(int,input().split())
mod = 998244353
a = [0]*(K+1)
b = [0]*(K+1)
c = [0]*(K+1)
d = [0]*(K+1)
if sx == gx and sy == gy:
    a[0] = 1
elif sy == gy:
    b[0] = 1
elif sx == gx:
    c[0] = 1
else:
    d[0] = 1

for i in range(K):
    a[i+1] = (b[i] + c[i])%mod
    b[i+1] = (a[i]*(H-1) + b[i]*(H-2) + d[i])%mod
    c[i+1] = (a[i]*(W-1) + c[i]*(W-2) + d[i])%mod
    d[i+1] = (b[i]*(W-1) + c[i]*(H-1) + d[i]*(H+W-4))%mod

print(a[K])
# print(a,b,c,d)    

