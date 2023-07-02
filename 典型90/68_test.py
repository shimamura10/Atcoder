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
f = open("C:\\Users\\heilab\\Downloads\\01_random_2.txt", "r")
datalist = f.readlines()
N = int(datalist[0])
Q = int(datalist[1])
A = [0]*N
sum = [0]*N
uft = UnionFind(N)
q = [list(map(int,datalist[2+i].split())) for i in range(Q)]
amb = [False]*Q
i = 0
for t,x,y,v in q:
    x -= 1
    y -= 1
    if t == 0:
        uft.union(x,y)
        sum[x] = v
    else:
        if not uft.same(x,y):
            amb[i] = True
    i += 1
for i in range(1,N):
    A[i] = sum[i-1] - A[i-1]
i = 0
evenbit = BIT(N)
oddbit = BIT(N)
uft = UnionFind(N+1)
seen = [False]*(N+1)
for t,x,y,v in q:
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
                ans2 = v - ss + sb
            else:
                ans2 = v + ss - sb
        else:
            ans2 = ss - sb - v
        if not uft.same(x,y):
            ans2 = "Ambiguous"
        x -= 1
        y -= 1
        if amb[i]:
            ans1 = 'Ambiguous'
        else:
            if (y-x)%2 == 0:
                ans1 = A[y] + v - A[x]
            else:
                ans1 = A[y] - v + A[x]
        if ans1 != ans2:
            print(i,x+1,y+1,v)
            print(ans1, ans2)
    i += 1