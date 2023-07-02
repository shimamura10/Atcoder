N = int(input())
def f(a,b):
    return (b-a+1)*(a+b)//2
ans = 0
for i in range(N):
    a,b = map(int,input().split())
    ans += f(a,b)
print(ans)