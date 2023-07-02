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
N,M,K = map(int,input().split())
uft = UnionFind(N)
F = [[] for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    F[a].append(b)
    F[b].append(a)
    uft.union(a,b)
B = [[] for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    B[a].append(b)
    B[b].append(a)
ans = [0]*N
for i in range(N):
    ans[i] += uft.size(i) - len(F[i]) - 1
for i in range(N):
    for b in B[i]:
        if uft.same(i,b):
            ans[i] -= 1
print(*ans)
