X,Y,A,B = map(int,input().split())
ans = 0
s = X
# while True:
#     if s*(A-1) < B:
#         s *= A
#     else:
#         s += B
#     if s > Y:
#         break
#     ans += 1
while s*(A-1) < B:
    s *= A
    # print(s,ans)
    if s >= Y:
        s //= A
        break
    ans += 1
if (Y-s)%B == 0 and Y-s >= B:
    ans += (Y-s)//B - 1
    # print(ans,s)
else:
    ans += (Y-s)//B
    # print(ans,s)

print(ans)