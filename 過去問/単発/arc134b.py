N = int(input())
S = input()
dict = {}
S_list = []
for i in range(N):
    if not S[i] in dict.keys():
        dict[S[i]] = [i]
    else:
        dict[S[i]].append(i)
    S_list.append(S[i])
ABC = 'abcdefghijklmnopqrstuvwxyz'
# x = []
i = 0
n = N-1
for s in ABC:
    if not s in dict.keys():
        continue
    while len(dict[s]) != 0:
        if dict[s][-1] > n:
            del dict[s][-1]
            continue
        while s == S[i] and i < N-1:
            i += 1
        
        if dict[s][-1] <= i:
            break
        n = dict[s][-1]
        # x += [i,n]
        a = S_list[i]
        b = S_list[n]
        S_list[i] = b
        S_list[n] = a
        # print(a,b)
        # print(n,i)
        # if n - i <= 1:
        #     break
        del dict[s][-1]
        i += 1
    if n - i <= 1:
        break
ans = ''
for i in range(N):
    ans += S_list[i]
print(ans)
# print(dict['c'])
# print(dict['b'])
# print(n,i)

# a = ['a','b','c']
# print(*a)

# a = 'abcd'
# for i in a:
#     print(i)
# mydict = {"apple":[1,2], "orange":2, "banana":3}

# mydict["apple"].append(3)
# val = mydict["apple"]
# print(val)