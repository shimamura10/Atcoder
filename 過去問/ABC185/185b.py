N,M,T = map(int,input().split())
time = 0
butt = N
for i in range(M):
    a,b = map(int,input().split())
    butt -= a-time
    if butt <= 0:
        ans = 'No'
        break
    butt += b-a
    if butt > N:
        butt = N  
    time = b
if butt > T - time:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)