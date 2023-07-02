N = int(input())
A = list(map(int,input().split()))
ans = N
t = 0
for a in A[::-1]:
    t += a
    if t < 4:
        ans -= 1
    else:
        break
print(ans)