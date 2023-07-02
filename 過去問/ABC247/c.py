N = int(input())
ans = []
for i in range(1,N+1):
    ans = ans + [i] + ans
print(*ans)