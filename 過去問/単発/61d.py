N,M = map(int,input().split())
inf = float('inf')
class BellmanFord():
    def __init__(self, N):
        self.N = N
        self.edges = []

    def add(self, u, v, d, directed=False):
        """
        u = from, v = to, d = cost
        directed = Trueのとき、有向グラフである。
        """
        if directed is False:
            self.edges.append([u, v, d])
            self.edges.append([v, u, d])
        else:
            self.edges.append([u, v, d])


    def BellmanFord_search(self, start):
        D = [inf for i in range(self.N)]
        D[start] = 0
        for i in range(self.N*2):
            for u,v,d in self.edges:
                if D[v] > D[u] + d:
                    D[v] = D[u] + d
                    if i>=self.N:
                        D[v]=-inf
        return D
bf = BellmanFord(N)
for i in range(M):
    a,b,c = map(int,input().split())
    bf.add(a-1,b-1,-c,True)
ans = -bf.BellmanFord_search(0)[-1]
# print(bf.BellmanFord_search(0))
print(ans)