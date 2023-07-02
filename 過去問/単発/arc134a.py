N,L,W = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
r = 0
for i in range(N):
    l = a[i] - r 
    if l > 0:
        if l % W != 0:
            ans += l//W + 1
        else:
            ans += l//W
    r = a[i] + W
    # print(r,l)
l = L - r 
if l > 0:
    if l % W != 0:
        ans += l//W + 1
    else:
        ans += l//W
print(ans)
