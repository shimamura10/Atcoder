from math import sqrt
# print(int(sqrt(47)))
N = int(input())
a = int(sqrt(N))
n = [N]
ans = 0
# if a + 1 == N//a:
#     ans += N//a*2 + 1
if a == N//a:
    ans -= N//a
for i in range(1,a+1):
    n.append(N//(i+1))
    ans += (n[i-1]-n[i])*i
    ans += N//i
print(ans)
# print(3//2)