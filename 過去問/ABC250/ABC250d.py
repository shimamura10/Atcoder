from bisect import bisect_right


def eratosthenes(n):
    res=[0 for i in range(n+1)]
    prime=set([])
    for i in range(2,n+1):
        if not res[i]:
            prime.add(i)
            for j in range(1,n//i+1):
                res[i*j]=1
    prime = list(prime)
    prime.sort()
    return prime
N = int(input())
P = eratosthenes(int(N**(1/3))+10)
ans = 0
for i,q in enumerate(P):
    p = N//(q**3)
    n = bisect_right(P,p)
    ans += min(i,n)
print(ans)