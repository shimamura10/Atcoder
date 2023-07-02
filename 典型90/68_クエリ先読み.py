# class SegmentTree:
#     def __init__(self, init_val, segfunc, ide_ele):  #init_val:葉に持たせる初期値を格納したリスト
#         n = len(init_val)  #要素数
#         self.segfunc = segfunc  #子を引数とした親のノードを更新する関数
#         self.ide_ele = ide_ele  #初期値
#         self.num = 1 << (n - 1).bit_length()  #完全二分木に必要な葉の数
#         self.tree = [ide_ele] * 2 * self.num
#         self.size = n
#         for i in range(n):
#             self.tree[self.num + i] = init_val[i]
#         for i in range(self.num - 1, 0, -1):
#             self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

#     def update(self, k, x):  #k番目の要素のノードをxに更新(kは始めを0として数える)
#         k += self.num
#         self.tree[k] = x
#         while k > 1:
#             k >>= 1
#             self.tree[k] = self.segfunc(self.tree[2*k], self.tree[2*k+1])

#     def query(self, l, r):  #l<=n<r番目の要素についてクエリを実行
#         if r==self.size:    #l,rは始めの要素を0として数える
#             r = self.num    #全範囲はl=0,r=Nのとき

#         res = self.ide_ele

#         l += self.num
#         r += self.num
#         right = []
#         while l < r:
#             if l & 1:
#                 res = self.segfunc(res, self.tree[l])
#                 l += 1
#             if r & 1:
#                 right.append(self.tree[r-1])
#             l >>= 1
#             r >>= 1

#         for e in right[::-1]:
#             res = self.segfunc(res,e)
#         return res

# N = int(input())
# Q = int(input())
# inf = float('inf')
# def segfunc(x,y):
#     return x+y
# init1 = []
# init2 = []
# for i in range(N-1):
#     if i%2 == 0:
#         init1.append(inf)
#         init2.append(0)
#     else:
#         init1.append(0)
#         init2.append(inf)
# smt1 = SegmentTree(init1,segfunc,0)
# smt2 = SegmentTree(init2,segfunc,0)
# for _ in range(Q):
#     t,x,y,v = map(int,input().split())
#     x -= 1
#     y -= 1
#     if t == 0:
#         if x%2 == 0:
#             smt1.update(x,v)
#         else:
#             smt2.update(x,v)
#     elif t == 1:
#         if x == y:
#             print(v)
#             continue
#         a = smt1.query(min(x,y),max(x,y))
#         b = smt2.query(min(x,y),max(x,y))
#         d = a - b
#         if x < y:
#             if x % 2 == 0:
#                 if (y-x)%2 == 0:
#                     ans = v - d #
#                 else:
#                     ans = d - v #
#             else:
#                 d *= -1
#                 if (y-x)%2 == 0:
#                     ans = v - d#
#                 else:
#                     ans = d - v#
#         else:
#             if y % 2 == 0:
#                 if (y-x)%2 == 0:
#                     ans = v + d
#                 else:
#                     ans = d - v   #
#             else:
#                 d *= -1
#                 if (y-x)%2 == 0:
#                     ans = v + d#
#                 else:
#                     ans = d - v#
#         if abs(ans) == inf:
#             print('Ambiguous')
#         else:
#             print(ans)
#         # a = smt.query(nx,ny)
#         # if a == inf:
#         #     print('Ambiguous')
#         # else:
#         #     vx = smt.query(nx,nx+1)
#         #     vy = smt.query(ny-1,ny)
#         #     print(2*(vx+vy)-a-v)



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
A = [0]*N
sum = [0]*N
uft = UnionFind(N)
q = [list(map(int,input().split())) for _ in range(Q)]
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
for t,x,y,v in q:
    if t == 1:
        x -= 1
        y -= 1
        if amb[i]:
            print('Ambiguous')
        else:
            if (y-x)%2 == 0:
                print(A[y] + v - A[x])
            else:
                print(A[y] - v + A[x])
    i += 1
    
    
