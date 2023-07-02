S = input()
T = input()
# j = 0
# if len(S) > len(T):
#     print("No")
#     exit()
# for i,t in enumerate(T):
#     if j < len(S) and t == S[j]:
#         j += 1
#         continue
#     else:
#         if j < len(S) and j >= 2 and S[j-1] == t and S[j-2] == t:
#             continue
#         else:
#             print("No")
#             exit()
# if j == len(S):
#     print("Yes")
# else:
#     print("No")

now = S[0]
cnt = 0
tpos = 0
for s in S:
    if s == now:
        cnt += 1
    else:
        if T[tpos] != now:
            print("No")
            exit()
        else:
            cntt = 0
            while tpos < len(T) and now == T[tpos]:
                cntt += 1
                tpos += 1
            if cnt != cntt and (cnt < 2 or cntt <= cnt):
                print("No")
                exit()
            now = s
            cnt = 1
cntt = 0
while tpos < len(T) and now == T[tpos]:
    cntt += 1
    tpos += 1
if cnt != cntt and (cnt < 2 or cntt <= cnt):
    print("No")
    exit()
if tpos == len(T):
    print("Yes")
else:
    print("No")