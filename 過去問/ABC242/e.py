T = int(input())
orda = ord('A')
mod = 998244353
for _ in range(T):
    N = int(input())
    S = input()
    ans = 0
    n = (N+1)//2
    for i in range(n):
        ans = ((ord(S[i])-orda)*pow(26,n-i-1,mod)+ans)%mod
    for i in range(n,N):
        a = S[i]
        b = S[2*n-i-(1+N%2)]
        if ord(S[i]) < ord(S[2*n-i-(1+N%2)]):
            break
        elif ord(S[i]) > ord(S[2*n-i-(1+N%2)]):
            ans += 1
            break
        if i == N-1:
            ans += 1
    print(ans%mod)
