N = int(input())
A = list(map(int,input().split()))
ans = 1
# stack = [[A[0],1]]
kind = [A[0]]
num = [1]
print(ans)
for i in range(1,N):
    a = A[i]
    k = num[-1]
    if kind[-1] == a:
        k += 1
        num[-1] = k
        if k < a:
            ans += 1
        else:
            ans -= k-1
            del kind[-1]
            del num[-1]
    else:
        kind.append(a)
        num.append(1)
        ans += 1
    print(ans)

# a = [[1,2,3]]
# # del a[-1]
# print(type(a[0]))
        