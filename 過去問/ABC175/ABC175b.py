N = int(input())
L = list(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]:
                continue
            l = [L[i],L[j],L[k]]
            l.sort()
            if l[-1] < l[0] + l[1]:
                ans += 1
print(ans)