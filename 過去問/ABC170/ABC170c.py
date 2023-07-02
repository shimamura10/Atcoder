X,N = map(int,input().split())
p = set(map(int,input().split()))
ans = 0
for i in range(102):
    if i in p:
        continue
    if abs(ans-X) > abs(i-X):
        ans = i
print(ans)
