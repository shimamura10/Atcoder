from copy import copy


X = input()
ans = 10*int(X)
for i in range(int(X[0]),10):
    for d in range(-9,10):
        upper = False
        ok = True
        tmp = ""
        t = i
        for j in range(len(X)):
            tmp += str(t)
            if t > int(X[j]):
                upper = True
            elif t < int(X[j]) and not upper:
                ok = False
                break
            if t < 0:
                ok = False
                break
            t += d
            
        if ok:
            ans = min(ans,int(tmp))
print(ans)