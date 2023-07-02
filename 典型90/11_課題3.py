N = int(input())
job = [list(map(int,input().split())) for _ in range(N)]
job.sort()
C = job[-1][0] + 1
value = [[0]*C for _ in range(N+1)]
for i in range(1,N+1):
    d,c,s = job[i-1]
    for j in range(1,C):
        if j >= c and j <= d:
            value[i][j] = max(value[i-1][j-c]+s, value[i-1][j])
        else:
            value[i][j] = value[i-1][j]
ans = 0
for v in value[-1]:
    ans = max(ans,v)
print(ans)