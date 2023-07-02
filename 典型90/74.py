N = int(input())
S = input()
A = [ord(s) - ord('a') for s in S]
ans = 0
for i,a in enumerate(A):
    ans += a*(1<<i)
print(ans)
# r = -1
# for i in range(N):
#     i = N - i - 1
#     if A[i] > 0:
#         r = i
# ans = 0
# for i in range(r):
#     ans += A[i]
#     A[i] = 0
# while r >= 0: