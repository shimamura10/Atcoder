a,b,c,x = map(int,input().split())
if x <= a:
    ans = 1
elif x <= b:
    ans = c/(b-a)
else:
    ans = 0
print(ans)