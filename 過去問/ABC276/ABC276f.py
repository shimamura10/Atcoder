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
    ans = []
    for i,n in enumerate(l):
        ans.append(i - bit.query(n))
        bit.update(n,1)
    return ans

N = int(input())
A = list(map(int,input().split()))
mod = 998244353
S = [0]
bit = BIT(max(A))
l = tenntou(A)
# print(l)
acc = 0
for i,a in enumerate(A):
    tmp = (i-l[i])*a
    tmp += acc - bit.query(a)
    S.append((S[-1] + 2*tmp + a)%mod)
    acc += a
    bit.update(a,a)
for i in range(1,N+1):
    div = pow(i**2, mod-2, mod)
    print((S[i]*div)%mod)