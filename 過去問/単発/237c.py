s = input()
n = len(s)
num_a_r = 0
num_a_f = 0
result = []
for i in range(n):
    if s[n-i-1] == "a":
        num_a_r += 1
    else:
        break
for i in range(n):
    if s[i] == "a":
        num_a_f += 1
    else:
        break
k = num_a_r - num_a_f
if k>=0: 
    t = "a"*(k) + s
    revt = t[::-1]
    if t == revt:
        result = "Yes"
if result == []:
    result = "No"
print(result)
    # c = 0
    # j = i
#     while c == 0 and j < (n+i)/2:
#         if t[j] != t[n+i-1-j]:
#             c += 1
#         j += 1
#     if c == 0:
#         print("Yes")
#         break
# if c != 0:
#     print("No")