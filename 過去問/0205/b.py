n = int(input())
a = list(map(int, input().split()))
c = [0]
for i in range(n):
    if c[i] + a[i]>=360:
        c.append(a[i]+c[i]-360)
    else:
        c.append(a[i]+c[i])
sortc = sorted(c)
ans = 0
if sortc[n]<=180:
    ans = 360-sortc[n]
else:
    for i in range(n):
        if sortc[i+1] - sortc[i]>ans:
            ans = sortc[i+1] - sortc[i]
print(ans)
