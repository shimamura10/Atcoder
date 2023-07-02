from collections import deque


N = int(input())
A = list(map(int,input().split()))
s = sum(A)
s //= 10
q = deque()
l = 0
r = 0
sum = 0
while True:
    q.append(A[r])
    sum += A[r]
    r = (r+1)%N
    if sum == s:
        print('Yes')
        exit()
    while sum > s:
        a = q.popleft()
        l += 1
        sum -= a
    if l >= N:
        break
print('No')
    
