from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
Q = int(input())
que = []
for i in range(Q):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    que.append((x,y,i))
que.sort()
ans = [-1]*Q
seena = defaultdict(int)
seenb = defaultdict(int)
b = 0
q = 0
l = 10**6
r = 0
unseen = set()
for i in range(N):
    seena[A[i]] = 1
    if A[i] in unseen:
        unseen.discard(A[i])
    if not seenb[A[i]]:
        while b < N:
            seenb[B[b]] = 1
            if not seena[B[b]]:
                unseen.add(B[b])
            if B[b] == A[i]:
                if len(unseen) == 0:
                    l = b
                else:
                    l = 10**6
                break
            b += 1
    while b < N:
        if not seena[B[b]]:
            r = b
            break
        b += 1
    while q < Q:
        x,y,idx = que[q]
        if x != i:
            break
        if y >= l and y < r:
            ans[idx] = 1
        else:
            ans[idx] = 0
        q += 1
for a in ans:
    if a:
        print('Yes')
    else:
        print('No')
            
            