N = int(input())
job = [list(map(int,input().split())) for _ in range(N)]
job.sort()
ans = 0
for bit in range(1<<N):
    tmp = 0
    now = 0
    for i,j in enumerate(job):
        if bit >> i  & 1:
            d,c,s = j
            if d-now >= c:
                tmp += s
                now += c
            else:
                break
    ans = max(ans,tmp)
print(ans)