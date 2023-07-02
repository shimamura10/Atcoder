
N = int(input())
C = list(map(int,input().split()))
C = sorted(C,reverse=True)
ans = 0
mod = 10**9+7
p = [1]  #p[i]は2**i
for i in range(N):
    p.append(p[-1]*2%mod)
f = [0]  #f[i]は2**i未満の二進数に登場する1の数の和
for i in range(N-1):
    f.append((2*f[-1]+p[i])%mod)
ans = 0
for i,c in enumerate(C):
    ans += (f[i]+p[i])%mod*c%mod*p[N-i-1]  
    #f[i]+p[i]はi-1番目までで異なるところがD個としたときのΣD=(0,i)(cmb(i,d)*(D+1))
    #p[N-i-1]はi+1番目以降の異なるところの組み合わせの数
    ans %= mod
ans *= p[N]  #片方の数列が何通りあるか
ans %= mod
print(ans)