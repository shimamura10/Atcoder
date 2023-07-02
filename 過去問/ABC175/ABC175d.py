N,K = map(int,input().split())
P = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = -float('inf')
for i in range(N):
    sum = [0]
    seen = [-1]*N
    ind = i
    n = 0
    for j in range(min(K,N)):
        ind = P[ind] - 1
        if seen[ind] >= 0:
            n = j - seen[ind]
            break
        seen[ind] = j
        sum.append(sum[-1]+C[ind])
        if j == min(K,N) - 1:
            n = min(K,N)
            ind = P[i] - 1
    cycle = sum[-1] - sum[-(1+n)]
    K -= seen[ind]
    if cycle > 0:
        tmp = cycle*(K//n) + max(sum[-(1+n):K%n-n])
        tmp = max(tmp,max(sum),cycle*(K//n-1) + max(sum[-(1+n):min(K+n,len(sum))]))
    else:
        del sum[0]
        tmp = max(sum)
    ans = max(ans,tmp)
print(ans)
    
