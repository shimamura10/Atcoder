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
import heapq
N,M = map(int,input().split())
G = []
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    heapq.heappush(G,(-a,b))

tree = UnionFindVerSize(N)
i = N
used = set()
ans = []
for _ in range(M):
    a,b = heapq.heappop(G)
    a *= -1
    while a != i:        
        # ans.append(tree.group-(N-len(used)))
        ans.append(tree.group-(i))
        # print(tree.group,(i))
        # print(used)
        i -= 1
    # if tree._parent[a] == a and tree._parent[b] == b:
    #     group += 1
    # if not tree.is_same_group(a,b) and tree._parent[a] != a: 
    #     group -= 1
    tree.unite(a,b)
    used.add(a)
    used.add(b)
    # group += 1
    
    
while i > 0:
    # ans.append(tree.group-(N-len(used)))
    ans.append(tree.group-i)
    i -= 1
for i in range(N):
    print(ans[-(i+1)])
# print(ans)
    

    