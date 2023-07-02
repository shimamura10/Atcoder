P = int(input())
A = [1]
for i in range(2,20):
    A.append(A[-1]*i)
ans = 0
for a in A[::-1]:
    ans += P//a
    P %= a
print(ans)