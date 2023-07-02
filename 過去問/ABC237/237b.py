hw = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(hw[0])]
# print(a)
b = [[0]*hw[0] for i in range(hw[1])]
for i in range(hw[1]):
    for j in range(hw[0]):
        b[i][j] = a[j][i]
for i in range(hw[1]):
    # print(*b[i])
    s = [str(j) for j in b[i]]
    print(" ".join(s))

