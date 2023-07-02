class WeightedUnionFind():
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
        self.val = [0 for i in range(N)]
        self.flag = True
        self.edge = [[] for i in range(N)]

    def dfs(self,v,pv):
        stack = [(v,pv)]
        new_parent = self.parent[pv]
        while stack:
            v,pv = stack.pop()
            self.parent[v] = new_parent
            for nv,w in self.edge[v]:
                if nv!=pv:
                    self.val[nv] = self.val[v] + w
                    stack.append((nv,v))

    def unite(self,x,y,w):
        if not self.flag:
            return
        if self.parent[x]==self.parent[y]:
            self.flag = (self.val[x] - self.val[y] == w)
            return

        if self.size[self.parent[x]]>self.size[self.parent[y]]:
            self.edge[x].append((y,-w))
            self.edge[y].append((x,w))
            self.size[x] += self.size[y]
            self.val[y] = self.val[x] - w
            self.dfs(y,x)
        else:
            self.edge[x].append((y,-w))
            self.edge[y].append((x,w))
            self.size[y] += self.size[x]
            self.val[x] = self.val[y] + w
            self.dfs(x,y)
N,M = map(int,input().split())
wufd = WeightedUnionFind(N)
for i in range(M):
    l,r,d = map(int,input().split())
    l -= 1
    r -= 1
    wufd.unite(l,r,d)
for i in range(N):
    if not wufd.flag:
        print('No')
        exit()
print('Yes')
print(wufd.val)
print(wufd.val[1]-wufd.val[0])