#自分より左にあるのに自分より数が大きいものの組の数
#バブルソートの交換回数と同じ
# （バブルソートで一回交換をすると必ず転倒数が1小さくなるため）

#i以下の数がいくつでてきたかをi番目の要素にもつBITを使うとO(NlogN)で計算できる
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

def tenntou(l):  #lの要素は1以上、重複は可、O(NlogN)
    bit = BIT(max(l))
    ans = 0
    for i,n in enumerate(l):
        ans += i - bit.query(n)
        bit.update(n,1)
    return ans
