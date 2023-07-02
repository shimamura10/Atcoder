from itertools import accumulate


N,K = map(int,input().split())
A = list(map(int,input().split()))
Q = int(input())
dif = [A[i+1]-A[i] for i in range(N-1)]
moddif = [[] for i in range(K)]
for i in range(N-1):
    moddif[i%K].append(dif[i])
summoddif = [[0] + list(accumulate(moddif[i])) for i in range(K)]
for i in range(Q):
    ok = True
    l, r = map(int,input().split())
    l -= 1
    r -= 1
    cnt = 0
    for n in range(l, r):
        if cnt == K:
            break
        cnt += 1
        i = n%K
        j = (n-i)//K
        sn = (r-1-n)//K
        # S = sum(moddif[i][j:j+sn+1])
        S = summoddif[i][j+sn+1] - summoddif[i][j]
        if (i == (l+K-1)%K):
            S += A[l]
        if (i == (r-K)%K):
            S -= A[r]
        if S != 0:
            ok = False
    if ok:
        print("Yes")
    else:
        print("No")