N,M = map(int,input().split())
A = list(map(int,input().split()))
stack = []
ans = []
for i in range(N):
    i += 1
    if i not in A:
        ans.append(i)
        ans += stack[::-1]
        stack = []
    else:
        stack.append(i)
print(*ans)