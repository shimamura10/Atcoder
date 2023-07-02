
import collections
import heapq


class Dijkstra():
    def __init__(self):
        self.e = collections.defaultdict(list)

    def add(self, u, v, d, directed=False):
        """
        #0-indexedでなくてもよいことに注意
        #u = from, v = to, d = cost
        #directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.e[u].append([v, d])
            self.e[v].append([u, d])
        else:
            self.e[u].append([v, d])

    def delete(self, u, v):
        self.e[u] = [_ for _ in self.e[u] if _[0] != v]
        self.e[v] = [_ for _ in self.e[v] if _[0] != u]

    def Dijkstra_search(self, s):
        """
        #0-indexedでなくてもよいことに注意
        #:param s: 始点
        #:return: 始点から各点までの最短経路と最短経路を求めるのに必要なprev
        """
        d = collections.defaultdict(lambda: float('inf'))
        prev = collections.defaultdict(lambda: None)
        d[s] = 0
        q = []
        heapq.heappush(q, (0, s))
        v = collections.defaultdict(bool)
        while len(q):
            k, u = heapq.heappop(q)
            if v[u]:
                continue
            v[u] = True

            for uv, ud in self.e[u]:
                if v[uv]:
                    continue
                vd = k + ud
                if d[uv] > vd:
                    d[uv] = vd
                    prev[uv] = u
                    heapq.heappush(q, (vd, uv))

        return d

    def getDijkstraShortestPath(self, start, goal):
        _, prev = self.Dijkstra_search(start)
        shortestPath = []
        node = goal
        while node is not None:
            shortestPath.append(node)
            node = prev[node]
        return shortestPath[::-1]
djk = Dijkstra()
N,M = map(int,input().split())
G = [[] for _ in range(N)]
unpair = []
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if a == -1:
        unpair.append(b)
    else:
        djk.add(a,b,1)
inf = float('inf')
dis1 = djk.Dijkstra_search(0)
disN = djk.Dijkstra_search(N-1)
m1,mN = inf,inf
for i in unpair:
    m1 = min(m1,dis1[i])
    mN = min(mN,disN[i])
Ans = []
for i in range(N):
    ans = min(dis1[N-1],min(dis1[i],m1+1)+min(disN[i],mN+1))
    if ans >= inf:
        Ans.append(-1)
    else:
        Ans.append(ans)
print(*Ans)