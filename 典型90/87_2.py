class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)] for i in range(N)]  # d[u][v] : 辺uvのコスト(存在しないときはinf)

    def add(self, u, v, c, directed=False):
        """
        0-indexedであることに注意
        u = from, v = to, c = cost
        directed = Trueなら、有向グラフである
        """
        if directed is False:
            self.d[u][v] = c
            self.d[v][u] = c
        else:
            self.d[u][v] = c

    def WarshallFloyd_search(self):
        # これを d[i][j]: iからjへの最短距離 にする
        # 本来無向グラフでのみ全域木を考えるが、二重辺なら有向でも行けそう
        # d[i][i] < 0 なら、グラフは負のサイクルを持つ
        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    self.d[i][j] = min(
                        self.d[i][j], self.d[i][k] + self.d[k][j])
        for i in range(self.N):
            self.d[i][i] = 0
        return self.d   #hasNegativeCycle == True なら負閉路あり
N,P,K = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(N)]
def lessP(X):
    wf = WarshallFloyd(N)
    for i in range(N):
        for j in range(i):
            c = D[i][j]
            if c < 0:
                c = X
            wf.add(i,j,c)
    xd = wf.WarshallFloyd_search()
    ret = 0
    for i in range(N):
        for j in range(i):
            if xd[i][j] <= P:
                ret += 1
    return ret
if lessP(P+1) == K:
    print("Infinity")
    exit()
# if lessP(0) < K or lessP(P+1) > K:
#     print(0)
#     exit()
def lessK(x):
    if lessP(x) <= K:
        return True
    else:
        return False
def largerK(x):
    if lessP(x) >= K:
        return True
    else:
        return False
def binary_search(function,no,ok):  #mが条件を満たすかどうかを返す関数function
    while True:                     #条件を満たさない値no
        m = (no + ok)//2            #条件を満たす値ok
        if function(m):             #ギリギリ条件を満たすindexを返す
            ok = m
        else:
            no = m
        if abs(ok - no) == 1:
            return ok
sx = binary_search(lessK,0,P+1)
bx = binary_search(largerK,P+1,0)
print(bx-sx+1)