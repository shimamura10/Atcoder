class BIT():  #要素番号は始めを1としていることに注意
    def __init__(self,n,mod=0):
        self.BIT = [0]*(n+1)
        self.num = n
        self.mod = mod

    def query(self,idx):  #1からidx番目までの和を返す
        res_sum = 0
        mod = self.mod
        while idx > 0:
            res_sum += self.BIT[idx]
            if mod:
                res_sum %= mod
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):  #idx番目の要素にxを足す
        mod = self.mod
        while idx <= self.num:
            self.BIT[idx] += x
            if mod:
                self.BIT[idx] %= mod
            idx += idx&(-idx)
        return
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
N = int(input())
Q = int(input())        
evenbit = BIT(N)
oddbit = BIT(N)
uft = UnionFind(N+1)
seen = [False]*(N+1)
for i in range(Q):
    t,x,y,v = map(int,input().split())
    if t == 0 and (not seen[x]):
        if x % 2:
            oddbit.update(x,v)
        else:
            evenbit.update(x,v)
        uft.union(x,y)
        seen[x] = True
    if t == 1:
        m = min(x,y)
        M = max(x,y)
        if m%2:
            ss = oddbit.query(M-1) - oddbit.query(m-1)
            sb = evenbit.query(M-1) - evenbit.query(m-1)
        else:
            ss = evenbit.query(M-1) - evenbit.query(m-1)
            sb = oddbit.query(M-1) - oddbit.query(m-1)
        if x%2 == y%2:
            if x < y:
                ans = v - ss + sb
            else:
                ans = v + ss - sb
        else:
            ans = ss - sb - v
        if not uft.same(x,y):
            ans = "Ambiguous"
        print(ans)