from collections import defaultdict


N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [A[i] + B[i] for i in range(N)]
math = defaultdict(list)
eng = defaultdict(list)
s = defaultdict(list)
seen = [False]*N
ans = []
for i,a in enumerate(A):
    math[a].append(i)
for i,b in enumerate(B):
    eng[b].append(i)
for i,b in enumerate(C):
    s[b].append(i)
for a in sorted(A)[::-1]:
    if X == 0:
        break
    for x in math[a]:
        ans.append(x)
        seen[x] = True
        X -= 1
        if X == 0:
            break
    del math[a]
for b in sorted(B)[::-1]:
    if Y == 0:
        break
    for x in eng[b]:
        if not seen[x]:
            ans.append(x)
            seen[x] = True
            Y -= 1
            if Y == 0:
                break
    del eng[b]
    
for b in sorted(C)[::-1]:
    if Z == 0:
        break
    for x in s[b]:
        if not seen[x]:
            ans.append(x)
            seen[x] = True
            Z -= 1
            if Z == 0:
                break
    del s[b]
ans.sort()
for a in ans:
    print(a+1)
