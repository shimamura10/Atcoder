n=int(input())
a=list(map(int, input().split()))
mod=10**9+7
l=[0]*60
for i in range(n):
    for j in range(60):
        if 2**j>a[i]:
            continue 
        if (a[i]>>j)&1:
            l[j]+=1 
ans=0
for i in range(n):
    for j in range(60):
        if (a[i]>>j)&1:
            ans+=(2**j)*(n-l[j])
            continue
        # else:
            # ans+=(2**j)*l[j]
        ans%=mod
print(ans)