class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.cnt = [0] * n
        self.group = n
        

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        self.cnt[x] += 1
        if x == y:
            return
        self.group -= 1
        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.cnt[x] += self.cnt[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return self.group

    def all_group_members(self):
        dic = {r:[] for r in self.roots()}
        for i in range(self.n):
            dic[self.find(i)].append(i)
        return dic

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
def kruskal(V):
    es.sort()
    UFT = UnionFind(V)
    res = 0
    for e in es:
        if not UFT.same(e[1], e[2]):
            UFT.union(e[1], e[2])
            res += e[0]
            # if e[0] > 0:
            #     rec.append(i)
    return res


N,M = map(int,input().split())
A = list(map(int,input().split()))

def score(x,y,mod=M):
    return (pow(x,y,mod) + pow(y,x,mod)) % mod
es = []
for i in range(N):
    for j in range(i):
        es.append((-score(A[i], A[j]), i, j))

print(-kruskal(N))