class WeightedUnionFind():
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]  #rank
        self.val = [0 for i in range(N)]  #親を0としたときの子までの距離
        self.flag = True  #Falseなら偽情報あり
        self.edge = [[] for i in range(N)]

    def dfs(self,v,pv):  #edgeを先に作ってから実行すると、vが含まれる木のみ作られる。
        stack = [(v,pv)]
        new_parent = self.parent[pv]
        while stack:
            v,pv = stack.pop()
            self.parent[v] = new_parent
            for nv,w in self.edge[v]:
                if nv!=pv:
                    self.val[nv] = self.val[v] + w
                    stack.append((nv,v))

    def unite(self,x,y,w):  #unite(x,y,w)は、val[x]-val[y]=wとなるようにx,yを同じグループに入れる
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
