N = int(input())
mod = 10**9+7
a = pow(9,N,mod)
b = pow(8,N,mod)
c = pow(10,N,mod)
print((c-(2*a-b))%mod)