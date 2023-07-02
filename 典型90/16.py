N = int(input())
A,B,C = list(map(int,input().split()))
dp = [N]*10000
ans = 10000
for i in range(10000):
    for j in range(10000-i):
        if N-A*i-B*j >= 0 and (N-A*i-B*j)%C == 0:
            ans = min(ans,i+j+(N-A*i-B*j)//C)
print(ans)