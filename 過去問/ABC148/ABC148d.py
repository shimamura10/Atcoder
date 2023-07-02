N = int(input())
A = list(map(int,input().split()))
t = 0
ans = 0
for a in A:
    if a == t + 1:
        t += 1
    else:
        ans += 1
if t:
    print(ans)
else:
    print(-1)
