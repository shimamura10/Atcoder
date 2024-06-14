class SegmentTree:
    def __init__(self, init_val, segfunc, ide_ele):  #init_val:葉に持たせる初期値を格納したリスト
        n = len(init_val)  #要素数
        self.segfunc = segfunc  #子を引数とした親のノードを更新する関数
        self.ide_ele = ide_ele  #初期値
        self.num = 1 << (n - 1).bit_length()  #完全二分木に必要な葉の数
        self.tree = [ide_ele] * 2 * self.num
        self.size = n
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):  #k番目の要素のノードをxに更新(kは始めを0として数える)
        k += self.num
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = self.segfunc(self.tree[2*k], self.tree[2*k+1])

    def query(self, l, r):  #l<=n<r番目の要素についてクエリを実行
        if r==self.size:    #l,rは始めの要素を0として数える
            r = self.num    #全範囲はl=0,r=Nのとき

        res = self.ide_ele

        l += self.num
        r += self.num
        right = []
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                right.append(self.tree[r-1])
            l >>= 1
            r >>= 1

        for e in right[::-1]:
            res = self.segfunc(res,e)
        return res

    def bisect_l(self,l,r,x):
        l += self.num
        r += self.num
        Lmin = -1
        Rmin = -1
        while l<r:
            if l & 1:
                if self.tree[l] <= x and Lmin==-1:
                    Lmin = l
                l += 1
            if r & 1:
                if self.tree[r-1] <=x:
                    Rmin = r-1
            l >>= 1
            r >>= 1

        if Lmin != -1:
            pos = Lmin
            while pos<self.num:
                if self.tree[2 * pos] <=x:
                    pos = 2 * pos
                else:
                    pos = 2 * pos +1
            return pos-self.num
        elif Rmin != -1:
            pos = Rmin
            while pos<self.num:
                if self.tree[2 * pos] <=x:
                    pos = 2 * pos
                else:
                    pos = 2 * pos +1
            return pos-self.num
        else:
            return -1
N = int(input())
hwd = [sorted(list(map(int,input().split()))) for _ in range(N)]
def cmp(A):
    cmpB = sorted(set(A))
    cmpD = { v: i for i, v in enumerate(cmpB)}
    return cmpD
cmpH = cmp([hwd[i][0] for i in range(N)])
cmpW = cmp([hwd[i][1] for i in range(N)])
cmpD = cmp([hwd[i][2] for i in range(N)])
for i in range(N):
  hwd[i][0] = cmpH[hwd[i][0]]
  hwd[i][1] = cmpW[hwd[i][1]]
  hwd[i][2] = cmpD[hwd[i][2]]
smt = SegmentTree([N+1]*N,lambda a,b: min(a,b), N+1)
hwd.sort(key=lambda x:x[1], reverse=True)
hwd.sort()
for h,w,d in hwd:
  mind = smt.query(0, w)
  if mind < d:
    print('Yes')
    exit()
  smt.update(w,min(d,smt.query(w,w+1)))
print('No')