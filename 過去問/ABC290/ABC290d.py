from math import gcd


T = int(input())
for _ in range(T):
    N,D,K = map(int,input().split())
    K -= 1
    g = gcd(N,D)
    n = N//g
    print(K%n*D%N+K//n)