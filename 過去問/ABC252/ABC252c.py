N = int(input())
ans = 10**10
S = [input() for _ in range(N)]
for i in range(10):
    tmp = [0]*10
    i = str(i)
    for s in S:
        tmp[s.index(i)%10] += 1
    t = 0
    for i,tm in enumerate(tmp):
        t = max(t,10*(tm-1)+i)
    ans = min(ans,t)
print(ans)
        
    