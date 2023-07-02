s = input()
a = [0]*10
for i in range(len(s)):
    a[int(s[i])] += 1
# print(a)
if len(s) == 1:
    if a[8] == 1:
        print('Yes')
        exit()
if len(s) == 2:
    for i in range(1,10):
        a[i] -= 1
        if a[i] < 0:
            a[i] += 1
            continue
        for j in range(1,10):
            a[j] -= 1
            if a[j] < 0:
                a[j] += 1
                continue
            if (j*10 + i)%8 == 0:
                print("Yes")
                exit()
            a[j] += 1
        a[i] += 1
if len(s) > 2:
    for i in range(1,10):
        a[i] -= 1
        if a[i] < 0:
            a[i] += 1
            continue
        for j in range(1,10):
            a[j] -= 1
            if a[j] < 0:
                a[j] += 1
                continue
            for k in range(1,10):
                a[k] -= 1
                if a[k] < 0:
                    a[k] += 1
                    continue
                if (100*k + 10*j + i)%8 == 0:
                    print('Yes')
                    exit()
                a[k] += 1
            a[j] += 1
        a[i] += 1
print('No')
# print(a)
# print(len(s))
