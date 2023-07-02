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
        d = [10**15] * self.V
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
    
    def shortest_path(self,t,prev):
        while t != -1:
            t = prev[t]
N,M = map(int,input().split())
djk = Dijkstra(N)
d = []
es = []
for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    djk.add_edge(a,b,c)
    djk.add_edge(b,a,c)
    es.append((a,b,c))

for i in range(N):
    d.append(djk.shortest_distance(i))
cnt = 0
for a,b,c in es:
    for i in range(N):
        if d[a][i] + d[i][b] <= c and a != i and b != i:
            cnt += 1
            break
print(cnt)
