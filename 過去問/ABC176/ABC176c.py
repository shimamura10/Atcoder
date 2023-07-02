N = int(input())
A = map(int,input().split())
ans = 0
tall = 0
for i in A:
    if tall > i:
        ans += tall - i
    else:
        tall = i
print(ans)