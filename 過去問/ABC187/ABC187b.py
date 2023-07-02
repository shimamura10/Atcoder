N = int(input())
P = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i):
        a = (P[j][1]-P[i][1])/(P[j][0]-P[i][0])
        if abs(a) <= 1:
            ans += 1
print(ans)