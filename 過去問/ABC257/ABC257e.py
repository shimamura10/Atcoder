N = int(input())
C = list(map(int,input().split()))
m = min(C)
r = N%m
ans = ''
cnt = N//m
while cnt > 0:
    for i in range(8,-1,-1):
        if C[i] <= r+m:
            ans += str(i+1)
            r -= C[i]-m
            break
    cnt -= 1
print(ans)