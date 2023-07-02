N = input()
k = len(N)
a = [0,0,0]
for i in range(k):
    a[int(N[i])%3] += 1
b = a[1] + 2*a[2]
if b%3 == 0:
    ans = 0
elif b%3 == 1:
    if a[1] > 0 and k > 1:
        ans = 1
    elif a[2] > 1 and k > 2:     
        ans = 2
    else:
        ans = -1
else:
    if a[2] > 0 and k > 1:
        ans = 1
    elif a[1] > 1 and k > 2:
        ans = 2
    else:
        ans = -1

print(ans)

# a = [1,2,3,3]
# print(sum(a))