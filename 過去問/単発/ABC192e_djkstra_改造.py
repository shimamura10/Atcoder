class Dijkstra():
    class Edge():
        def __init__(self, _to, _cost, _K):
            self.to = _to
            self.cost = _cost
            self.K = _K

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

    def add_edge(self, _from, _to, _cost, _K):
        self.G[_from].append(self.Edge(_to, _cost, _K))
        self._E += 1

    def shortest_distance(self, s):
        import heapq
        que = []
        d = [10**15] * self.V
        d[s] = 0
        prev = [-1] * self.V
        heapq.heappush(que, (0, s))

        while len(que) != 0:
            cost, v = heapq.heappop(que)
            if d[v] < cost: continue

            for i in range(len(self.G[v])):
                e = self.G[v][i]
                if d[v]%e.K == 0:
                    tmp = 0
                else:
                    tmp = e.K - d[v]%e.K
                e.cost += tmp
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
N,M,X,Y = map(int,input().split())
djk = Dijkstra(N)
for _ in range(M):
    a,b,t,k = map(int,input().split())
    a -= 1
    b -= 1
    djk.add_edge(a,b,t,k)
    djk.add_edge(b,a,t,k)
ans = djk.shortest_distance(X-1)[Y-1]
if ans == 10**15:
    print(-1)
else:
    print(ans)
