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
H,W = map(int,input().split())
Q = int(input())
uft = UnionFind(H*W)
seen = [[False]*W for _ in range(H)]
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        t,r,c = q
        r -= 1
        c -= 1
        seen[r][c] = True
        if r > 0:
            if seen[r-1][c]:
                uft.union((r-1)*W+c,r*W+c)
        if r < H-1:
            if seen[r+1][c]:
                uft.union((r+1)*W+c,r*W+c)
        if c > 0:
            if seen[r][c-1]:
                uft.union(r*W+c-1,r*W+c)
        if c < W-1:
            if seen[r][c+1]:
                uft.union(r*W+c+1,r*W+c)
    else:
        t,ra,ca,rb,cb = q
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        a = ra*W+ca
        b = rb*W+cb
        if seen[ra][ca] and seen[rb][cb] and uft.same(a,b):
            print('Yes')
        else:
            print('No')


H,W = map(int,input().split())
Q = int(input())
uft = UnionFind(H*W)
bit = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        t,r,c = q
        r -= 1
        c -= 1
        bit |= 1 << r*W + c
        if r > 0:
            if bit >> (r-1)*W + c & 1:
                uft.union((r-1)*W+c,r*W+c)
        if r < H-1:
            if bit >> (r+1)*W + c & 1:
                uft.union((r+1)*W+c,r*W+c)
        if c > 0:
            if bit >> r*W + c-1 & 1:
                uft.union(r*W+c-1,r*W+c)
        if c < W-1:
            if bit >> r*W + c+1 & 1:
                uft.union(r*W+c+1,r*W+c)
    else:
        t,ra,ca,rb,cb = q
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        a = ra*W+ca
        b = rb*W+cb
        if bit & 1 << a and bit & 1 << b and uft.same(a,b):
            print('Yes')
        else:
            print('No')
        
class UnionFindVerSize():
    def __init__(self, N):
        self._parent = [n for n in range(0, N)]
        self._size = [1] * N
        self.group = N

    def find_root(self, x):
        if self._parent[x] == x: return x
        self._parent[x] = self.find_root(self._parent[x])
        stack = [x]
        while self._parent[stack[-1]]!=stack[-1]:
            stack.append(self._parent[stack[-1]])
        for v in stack:
            self._parent[v] = stack[-1]
        return self._parent[x]

    def unite(self, x, y):
        gx = self.find_root(x)
        gy = self.find_root(y)
        if gx == gy: return

        self.group -= 1

        if self._size[gx] < self._size[gy]:
            self._parent[gx] = gy
            self._size[gy] += self._size[gx]
        else:
            self._parent[gy] = gx
            self._size[gx] += self._size[gy]

    def get_size(self, x):
        return self._size[self.find_root(x)]

    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

H,W = map(int,input().split())
Q = int(input())
uft = UnionFindVerSize(H*W)
bit = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        t,r,c = q
        r -= 1
        c -= 1
        bit |= 1 << r*W + c
        if r > 0:
            if bit >> (r-1)*W + c & 1:
                uft.unite((r-1)*W+c,r*W+c)
        if r < H-1:
            if bit >> (r+1)*W + c & 1:
                uft.unite((r+1)*W+c,r*W+c)
        if c > 0:
            if bit >> r*W + c-1 & 1:
                uft.unite(r*W+c-1,r*W+c)
        if c < W-1:
            if bit >> r*W + c+1 & 1:
                uft.unite(r*W+c+1,r*W+c)
    else:
        t,ra,ca,rb,cb = q
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        a = ra*W+ca
        b = rb*W+cb
        if bit & 1 << a and bit & 1 << b and uft.is_same_group(a,b):
            print('Yes')
        else:
            print('No')