from collections import deque
N,M = map(int,input().split())
K = []
A = []
dict = {}
for i in range(M):
    k = int(input())
    a = list(map(int,input().split()))
    K.append(k)
    A.append(a)
    if a[0] in dict:
        G = deque()
        G.append(i)
        G.append(dict[a[0]])
        while len(G):
            next = G.popleft()
            K[next] -= 1
            if K[next] == 0:
                continue
            if A[next][-K[next]] in dict:
                G.append(next)
                G.append(dict[A[next][-K[next]]])
            else:
                dict[A[next][-K[next]]] = next
    else:
        dict[a[0]] = i
for i in range(M):
    if K[i]:
        print('No')
        exit()
print('Yes')

    
