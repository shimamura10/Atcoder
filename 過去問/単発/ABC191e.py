import sys
sys.setrecursionlimit(100000000)
class Dijkstra():
    class Edge():
        def __init__(self, _to, _cost):
            self.to = _to
            self.cost = _cost

    def __init__(self, V):
        self.G = [[] for i in range(V)]
        self._E = 0
        self._V = V

    @property
    def E(self):
        return self._E

    @property
    def V(self):
        return self._V

    def add_edge(self, _from, _to, _cost):
        self.G[_from].append(self.Edge(_to, _cost))
        self._E += 1

    def shortest_distance(self, s):
        import heapq
        que = []
        d = [inf] * self.V
        d[s] = 0
        prev = [-1] * self.V
        heapq.heappush(que, (0, s))

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if d[e.to] > d[v] + e.cost:
                    d[e.to] = d[v] + e.cost
                    prev[e.to] = v
                    heapq.heappush(que, (d[e.to], e.to))
        return d
    
    def shortest_path(self,t,prev):  #tをゴールとする最短経路
        path = []
        while t != -1:
            path.append(t)
            t = prev[t]
        return path[::-1]
N,M = map(int,input().split())
djk = Dijkstra(N)
G = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    djk.add_edge(b,a,c)
    G[a].append((b,c))
inf = float('inf')
def dfs(v,s):
    if v == s:
        return 0
    if d[v] != -1:
        return d[v]
    if seen[v]:
        return inf
    if s == -1:
        s = v
    seen[v] = True
    res = inf
    for nv,c in G[v]:
        res = min(res,dfs(nv,s)+c)
    d[v] = res
    return res
for i in range(N):
    d = [-1]*N
    seen = [False]*N
    ans = dfs(i,-1)
    d[i] = 0
    nd = djk.shortest_distance(i)
    for i in range(N):
        if d[i] != -1 and d[i] != inf and d[i] != nd[i]:
            d[10**10] = 1
    if ans == inf:
        print(-1)
    else:
        print(ans)


