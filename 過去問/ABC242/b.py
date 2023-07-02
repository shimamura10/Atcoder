# from heapq import heappop, heappush


# # print(ord('a'))
# s = input()
# a = []
# for i in range(len(s)):
#     heappush(a,(ord(s[i]),i))
# ans = []
# # print(a)
# for i in range(len(s)):
#     b = heappop(a)
#     # print(b)
#     ans.append(s[b[1]])
# print(''.join(ans))

# print(ord('a'))

s = input()
a = []
for i in range(len(s)):
    a.append([ord(s[i]),i])
# print(a)
a.sort()
ans = []
for i in range(len(s)):
    ans.append(s[a[i][1]])
print(''.join(ans))
# print(*ans)

# s = input()
# ans = []
# for i in range(len(s)):
#     a.sort()
#     for j in range(len(s)):
#         a = 10**6
#         if ord(s[i]) < a:
#             a = 