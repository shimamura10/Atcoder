class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        self.d = [[float("inf") for i in range(N)]
                  for i in range(N)]  # d[u][v] : 辺uvのコスト(存在しないときはinf)

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
        # hasNegativeCycle = False
        # for i in range(self.N):
        #     if self.d[i][i] < 0:
        #         hasNegativeCycle = True
        #         break
        for i in range(self.N):
            self.d[i][i] = 0
        return self.d   #hasNegativeCycle == True なら負閉路あり
H,W = map(int,input().split())
S = [input() for _ in range(H)]
wf = WarshallFloyd(W*H)
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        if i + 1 < H and S[i+1][j] == '.':
            wf.add(i*W+j,(i+1)*W+j,1)
        if j + 1 < W and S[i][j+1] == '.':
            wf.add(i*W+j,i*W+j+1,1)
d = wf.WarshallFloyd_search()
ans = 0
for i in range(H*W):
    for j in range(H*W):
        if d[i][j] == float('inf'):
            continue
        ans = max(ans,d[i][j])
print(ans)