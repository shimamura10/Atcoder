from collections import defaultdict


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
    
    def shortest_path(self,t,prev):  #tをゴールとする最短経路
        path = []
        while t != -1:
            path.append(t)
            t = prev[t]
        return path[::-1]
N, M = map(int,input().split())
P = list(map(int,input().split()))
edge = [[] for _ in range(N)]
for i,p in enumerate(P):
  edge[p-1].append(i+1)
insurance = defaultdict(int)
for _ in range(M):
  x,y = map(int,input().split())
  x -= 1
  y += 1
  insurance[x] = max(insurance[x], y)
stack = [(0,insurance[0])]
isTarget = [False]*N
while stack:
  i, y = stack.pop()
  if y > 0:
    isTarget[i] = True
  for ni in edge[i]:
    stack.append((ni,max(insurance[ni], y-1)))
print(sum(isTarget))