from itertools import permutations


x = input()
y = input()
z = input()
dict = {}
for i in x:
    if not i in dict:
        dict[i] = -1
for i in y:
    if not i in dict:
        dict[i] = -1
for i in z:
    if not i in dict:
        dict[i] = -1
if len(dict) > 10:
    print('UNSOLVABLE')
    exit()
seen = [False for _ in range(10)]
n = len(dict)
for i in permutations(range(10),n):
    k = 0
    for j in dict:
        dict[j] = i[k]
        k += 1
    if dict[x[0]] == 0 or dict[y[0]] == 0 or dict[z[0]] == 0:
        continue
    a = 0
    for d in range(len(x)):
        a += dict[x[-(d+1)]]*10**d
    b = 0
    for d in range(len(y)):
        b += dict[y[-(d+1)]]*10**d
    c = 0
    for d in range(len(z)):
        c += dict[z[-(d+1)]]*10**d
    if a + b == c:
        print(a)
        print(b)
        print(c)
        exit()
print('UNSOLVABLE')