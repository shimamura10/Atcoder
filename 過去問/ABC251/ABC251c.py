N = int(input())
seen = set()
ans = 10**6
M = 0
for i in range(N):
    s,t = input().split()
    t = int(t)
    if s in seen:
        continue
    if M < t:
        ans = i+1
        M = t
    seen.add(s)
print(ans)