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
N = int(input())
P = list(map(int,input().split()))
mod = 
bit = BIT(N)
