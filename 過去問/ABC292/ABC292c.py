N = int(input())
cnt = [0]*(N+1)
for i in range(1,N):
    for j in range(1,N//i+1):
        cnt[i*j] += 1
# for i in range(1,N):
#     if i**2 >= N:
#         break
#     cnt[i**2] -= 1
ans = 0
for i in range(1,N):
    ans += cnt[i]*cnt[N-i]
print(ans)