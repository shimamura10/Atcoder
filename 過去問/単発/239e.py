N,Q = map(int,input().split())
x = list(map(int,input().split()))
G = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
q = [list(map(int,input().split())) for _ in range(Q)]
A = [[] for _ in range(N)]
def f(v,pv):
    a = [x[v]]
    for i in G[v]:
        if i == pv:
            continue
        a += f(i,v)
    a = sorted(a,reverse=True)
    A[v] = a
    return a
f(0,0)
for i in range(Q):
    print(A[q[i][0]-1][q[i][1]-1])

d = [[1,2]]
print(d[0][0])