class scc_graph:
 
    def __init__(self, N):
        self.N = N
        self.edges = []
 
    def csr(self):
        self.start = [0]*(self.N+1)
        self.elist = [0]*len(self.edges)
        for e in self.edges:
            self.start[e[0]+1] += 1
        for i in range(1, self.N+1):
            self.start[i] += self.start[i-1]
        counter = self.start[:]
        for e in self.edges:
            self.elist[counter[e[0]]] = e[1]
            counter[e[0]] += 1
 
    def add_edge(self, v, w):
        self.edges.append((v, w))
 
    def scc_ids(self):
        self.csr()
        N = self.N
        now_ord = group_num = 0
        visited = []
        low = [0]*N
        order = [-1]*N
        ids = [0]*N
        parent = [-1]*N
        stack = []
        for i in range(N):
            if order[i] == -1:
                stack.append(i)
                stack.append(i)
                while stack:
                    v = stack.pop()
                    if order[v] == -1:
                        low[v] = order[v] = now_ord
                        now_ord += 1
                        visited.append(v)
                        for i in range(self.start[v], self.start[v+1]):
                            to = self.elist[i]
                            if order[to] == -1:
                                stack.append(to)
                                stack.append(to)
                                parent[to] = v
                            else:
                                low[v] = min(low[v], order[to])
                    else:
                        if low[v] == order[v]:
                            while True:
                                u = visited.pop()
                                order[u] = N
                                ids[u] = group_num
                                if u == v:
                                    break
                            group_num += 1
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]], low[v])
        for i, x in enumerate(ids):
            ids[i] = group_num-1-x
 
        return group_num, ids
        #グループ数と、グループ番号を要素にしたリストを返す
        #グループ番号は、小さいほうが上位になっている。
        #つまり、グループ番号が大きいほうから小さいほうへは行けない
        #ループに入っていないものは単体のグループになる
 
    def scc_list(self):  #強連結成分のリストを要素にもつリストを返す
        group_num, ids = self.scc_ids()
        groups = [[] for _ in range(group_num)]
        for i, x in enumerate(ids):
            groups[x].append(i)
        return groups
N,M = map(int,input().split())
scc = scc_graph(N)
for _ in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    scc.add_edge(a,b)
ans = 0
for g in scc.scc_list():
    n = len(g)
    ans += n*(n-1)//2
print(ans)

