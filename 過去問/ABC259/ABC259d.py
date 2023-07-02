from math import sqrt

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
sx,sy,tx,ty = map(int,input().split())
start = []
goal = []
circle = []
for i in range(N):
    circle.append(list(map(int,input().split())))
uf = UnionFind(N)
def distance2(x1,y1,x2,y2):
    return (x1-x2)**2 + (y1-y2)**2
for i in range(N):
    xi,yi,ri = circle[i]
    if distance2(sx,sy,xi,yi) == ri**2:
        start.append(i)
    if distance2(tx,ty,xi,yi) == ri**2:
        goal.append(i)
    for j in range(i+1,N):
        xj,yj,rj = circle[j]
        d = distance2(xi,yi,xj,yj) 
        if d >= (ri-rj)**2 and d <= (ri+rj)**2:
            uf.union(i,j)
# print(uf.all_group_members())
for s in start:
    for g in goal:
        if uf.same(s,g):
            print("Yes")
            exit()
print("No")
