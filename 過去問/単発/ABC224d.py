from collections import defaultdict, deque


M = int(input())
G = [[] for _ in range(9)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
p = list(map(int,input().split()))
D = defaultdict(lambda:-1)
inis = '123456789'
que = deque()
que.append((inis,0))
def swap(i,j):
    ret = ''
    for k in range(9):
        if k == i:
            ret += s[j]
        elif k == j:
            ret += s[i]
        else:
            ret += s[k]
    return ret
while que:
    s,n = que.popleft()
    if D[s] != -1:
        continue
    D[s] = n
    for i in range(9):
        if s[i] == '9':
            ind = i
            break
    for i in G[ind]:
        ns = swap(ind,i)
        if D[ns] != -1:
            continue
        que.append((ns,n+1))
seen = [False]*10
for i in p:
    seen[i] = True
for i in range(1,10):
    if not seen[i]:
        p.append(i)
        break
stp = [-1]*9
for i in range(9):
    stp[p[i]-1] = i + 1
nstp = ''
for i in stp:
    nstp += str(i)
print(D[nstp])
