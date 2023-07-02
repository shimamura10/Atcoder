N,M = map(int,input().split())
ans = [-1]*N
for _ in range(M):
    s,c = map(int,input().split())
    s -= 1
    if ans[s] == -1 or ans[s] == c:
        ans[s] = c
    else:
        print(-1)
        exit()
# if N == 1 and ans[0] == -1:
#     print(0)
#     exit()
if ans[0] == 0 and N != 1:
    print(-1)
    exit()
if ans[0] == -1 and N != 1:
    ans[0] = 1
for i in range(N):
    if ans[i] == -1:
        ans[i] = 0
a = ''
for an in ans:
    a += str(an)
print(a)