from math import sqrt


N,K = map(int,input().split())
A = list(map(int,input().split()))
P = [list(map(int,input().split())) for _ in range(N)]
s = set(A)
ans = 0
for i in range(N):
    if i + 1 in s:
        continue
    x,y = P[i]
    tmp = 10**10
    for j in A:
        j -= 1
        tmp = min(tmp,sqrt((x-P[j][0])**2+(y-P[j][1])**2))
    ans = max(ans,tmp)
print(ans)
