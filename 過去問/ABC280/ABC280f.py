H,W = map(int,input().split())
ans = 0
for i in range(H):
    s = input()
    for a in s:
        if a == '#':
            ans += 1
print(ans)