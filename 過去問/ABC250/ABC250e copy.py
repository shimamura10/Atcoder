from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = int(input())
ca = []
cb = []
seena = set()
seenb = set()
for i,a in enumerate(A):
    if a in seena:
        continue
    seena.add(a)
    ca.append(i)
ca.append(N)
for i,b in enumerate(B):
    if b in seenb:
        continue
    seenb.add(b)
    cb.append(i)
cb.append(N)
que = []
for i in range(Q):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    que.append((x,y,i))
que.sort()
ans = [-1]*Q
a = 0
b = 0
unseenb = set()
seena = set()
seenb = set()
l = 0
r = 0
q = 0
for i,a in enumerate(ca):
    if i == len(ca)-1:
        continue
    seena.add(A[a])
    unseenb.discard(A[a])
    if not A[a] in seenb:
        while b < len(cb)-1:
            seenb.add(B[cb[b]])
            if not B[cb[b]] in seena:
                unseenb.add(B[cb[b]])
            if A[a] in seenb:
                break
            b += 1
    while q < Q:
        x,y,idx = que[q]
        if x >= ca[i+1]:
            break
        if y >= cb[b] and y < cb[b+1] and len(unseenb) == 0:
            ans[idx] = 1
        else:
            ans[idx] = 0
        q += 1
for a in ans:
    if a:
        print('Yes')
    else:
        print('No')