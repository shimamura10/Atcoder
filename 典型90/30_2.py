from collections import defaultdict


def eratosthenes(n):
    res=[0 for i in range(n+1)]
    prime=set([])
    for i in range(2,n+1):
        if not res[i]:
            prime.add(i)
            for j in range(1,n//i+1):
                res[i*j]=1
    return prime
N,K = map(int,input().split())
cnt = [0]*(N+1)
P = eratosthenes(N)
for p in P:
    tmp = p
    for i in range(N//p):
        cnt[tmp] += 1
        tmp += p
    # while tmp <= N:
    #     cnt[tmp] += 1
    #     tmp += p
ans = 0
for v in cnt:
    if v >= K:
        ans += 1
print(ans)
# print(len(P))