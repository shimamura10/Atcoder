T = int(input())
mod = 998244353
na = ord('A')
for _ in range(T):
    N = int(input())
    S = input()
    low = 0
    ok = True
    for i in range((N+1)//2):
        ns = ord(S[i])
        low *= 26
        low += ns-na
        low %= mod
        # low = (low+1)*(ns-na)%mod
    for i in reversed(range((N+1)//2)):
        if ord(S[i]) < ord(S[-(i+1)]):
            ok = True
            break
        if ord(S[i]) > ord(S[-(i+1)]):
            ok = False
            break
    low += ok
    print(low%mod)