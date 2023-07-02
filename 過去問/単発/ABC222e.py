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
        return d,prev
    
    def shortest_path(self,t,prev):  #tをゴールとする最短経路
        path = []
        while t != -1:
            path.append(t)
            t = prev[t]
        return path[::-1]

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
mod = 998244353
djk = Dijkstra(N)
cnt = {}
for _ in range(N-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    cnt[(a,b)] = 0
    djk.add_edge(a,b,1)
    djk.add_edge(b,a,1)
for i in range(M-1):
    d,prev = djk.shortest_distance(A[i]-1)
    path = djk.shortest_path(A[i+1]-1,prev)
    for j in range(len(path)-1):
        x = path[j]
        y = path[j+1]
        if (x,y) in cnt:
            cnt[(x,y)] += 1
        else:
            cnt[(y,x)] += 1
C = []
for v in cnt.values():
    C.append(v)
s = sum(C)
r = (s+K)//2
if (s+K)%2:
    print(0)
    exit()
b = r - K
tag = min(r,b)
if tag < 0:
    print(0)
    exit()
dp = [[0]*(tag+1) for _ in range(N)]
dp[0][0] = 1
for i in range(N-1):
    for j in range(tag+1):
        dp[i+1][j] = dp[i][j]
    for j in range(tag+1-C[i]):
        dp[i+1][j+C[i]] += dp[i][j]
        dp[i+1][j+C[i]] %= mod
print(dp[-1][-1])