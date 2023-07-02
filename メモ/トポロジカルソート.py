G = [[] for _ in range(N)]
indegree = [0]*N
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    indegree[b] += 1
stack = []
for i in range(N):
    if indegree[i] == 0:
        stack.append(i)
sort = []
while len(stack):
    v = stack.pop()
    sort.append(v)
    for j in G[v]:
        indegree[j] -= 1
        if indegree[j] == 0:
            stack.append(j)

l = [1,2]
l.pop()
print(l)