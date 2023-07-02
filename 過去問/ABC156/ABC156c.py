N = int(input())
X = list(map(int,input().split()))
ans = 10**10
for x in range(1,101):
    tmp = 0
    for i in range(N):
        tmp += (x-X[i])**2
    ans = min(ans,tmp)
print(ans)