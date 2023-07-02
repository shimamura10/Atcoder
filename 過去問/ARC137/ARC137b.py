N = int(input())
A = list(map(int,input().split()))
num0 = []
num1 = []
tmp = 0
n = 0
for i in range(N):
    if A[i] == tmp:
        n += 1
    else:
        if tmp == 0:
            num0.append(n)
        else:
            num1.append(n)
        tmp = 1 - tmp
        n = 1
if A[-1] == 1:
    num1.append(n)
else:
    num0.append(n)
l = 0
max0 = 0
tmp = 0
for i in range(len(num0)):
    tmp += num0[i]
    max0 = max(max0,tmp)
    if i == len(num1):
        break
    tmp -= num1[i]
    while tmp < 0:
        tmp += num1[l] - num0[l]
        l += 1
l = 0
max1 = 0
tmp = 0
for i in range(len(num1)):
    tmp += num1[i]
    max1 = max(max1,tmp)
    if i+1 == len(num0):
        break
    tmp -= num0[i+1]
    while tmp < 0:
        tmp += num0[l+1] - num1[l]
        l += 1
print(max1+max0+1)
