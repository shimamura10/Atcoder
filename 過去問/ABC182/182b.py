N = int(input())
A = list(map(int,input().split()))
ans = 2
sum_max = 0
m = max(A)
for i in range(2,m+1):
    sum = 0
    for j in range(N):
        if A[j]%i == 0:
            sum += 1
    if sum > sum_max:
        sum_max = sum
        ans = i
print(ans)
# a = [1,3,4,5]
# max(a)