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

    def update(self, k, x):  #k番目の要素のノードをxに更新
        k += self.num
        self.tree[k] = x
        while k > 1:
            k >>= 1
            self.tree[k] = self.segfunc(self.tree[2*k], self.tree[2*k+1])

    def query(self, l, r):  
        if r==self.size:
            r = self.num

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
W,N = map(int,input().split())
inf = 10**16
dp = [[0] + [-inf]*(W) for _ in range(N+1)]
def segfunc(x,y):
    return max(x,y)
smt = SegmentTree(dp[0],segfunc,-inf)
# seen = [[False]*(W+1) for _ in range(N+1)]
# for i in range(N+1):
#     seen[i][0] = True
for i in range(N):
    l,r,v = map(int,input().split())
    for j in range(W+1):
        # if j-r>=-1 and j-l<=W and seen[]:
        #     a = smt.query(j-r,j-l+1)
        
        if l <= j:
            a = smt.query(max(0,j-r),j-l+1)
            dp[i+1][j] = max(dp[i][j],a+v)
            # if dp[i+1][j] > 0:
            #     print(i,j,a)
        else:
            dp[i+1][j] = dp[i][j]
        # if l<=j and j <= r:
        #     # print(j,a)
        #     dp[i+1][j] = max(v,dp[i][j])
        # if j-r>=-1 and j-l<=W:
        #     a = smt.query(j-r,j-l+1)
        # # if a > 0:
        #     # if i == 1:
        #     #     print(j)
        #     if a > 0:
        #         dp[i+1][j] = max(dp[i][j],v+a)
        # if dp[i+1][j] == 0:
        #     dp[i+1][j] = dp[i][j]
    smt = SegmentTree(dp[i+1],segfunc,-inf)
ans = dp[N][W]
# print(dp[2][2000])
if ans > 0:
    print(ans)
else:
    print(-1)
# print(dp)
# for i in range(N):
#     a = []
#     for j in range(W+1):
        
#     print(dp[i+1])
# smt = SegmentTree([10,5,4,7,6],segfunc,0)
# print(smt.query(1,5))