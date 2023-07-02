N = int(input())
aok = 0
tak = []
for _ in range(N):
    a,b = map(int,input().split())
    aok += a
    tak.append(2*a+b)
tak.sort()
ans = 0
for t in tak[::-1]:
    if aok < 0:
        break
    aok -= t
    ans += 1
print(ans)