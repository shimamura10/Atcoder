N,M = map(int,input().split())
capacity = [[0]*N for _ in range(N)]

for i in range(M):
    u,v,c = map(int,input().split())
    capacity[u-1][v-1] = c

visited = [False for _ in range(N)]

def dfs_ff(s,e,flow):
    route.append(s)
    if (s==e):
        for i in range(len(route)-1):
            capacity[route[i]][route[i+1]] -= flow
            capacity[route[i+1]][route[i]] += flow
        return flow
    visited[s] = True
    for i in range(N):
        if capacity[s][i] > 0 and visited[i] == False:
            if capacity[s][i] < flow:
                flow = capacity[s][i]
            tmpflow = dfs_ff(i,e,flow)
            if tmpflow:
                return tmpflow
    del route[-1]
    return 0
max_flow = 0
while True:
    visited = [False]*N
    route = []
    f = dfs_ff(0,N-1,10**9)
    if not f: break
    max_flow += f
print(max_flow)