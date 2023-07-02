N = int(input())
A = []
for i in range(N):
    a = int(input())
    A.append([list(map(int,input().split())) for _ in range(a)])
ans = 0
for bit in range(1<<N):
    ok = True
    tmp = 0
    for i in range(N):
        if bit & 1<<i:
            tmp += 1
            for x,y in A[i]:
                x -= 1
                if (bit >> x & 1) != y:
                    ok = False
    if ok:
        ans = max(ans,tmp)
print(ans)