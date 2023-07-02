N = int(input())
P = [list(map(int,input().split())) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(i):
        ans += ((P[i][0]-P[j][0])**2+(P[i][1]-P[j][1])**2)**0.5
ans /= N/2
print(ans)