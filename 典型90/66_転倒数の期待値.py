N = int(input())
num = [0]*101
ans = 0
for _ in range(N):
    l,r = map(int,input().split())
    n = r-l+1
    for i in range(l,r+1):
        for j in range(i+1,101):
            ans += num[j]/n
        num[i] += 1/n
print(ans)