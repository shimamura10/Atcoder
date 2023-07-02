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
from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# bsort = sorted(B)
# trans = defaultdict(int)
# for i,b in enumerate(bsort):
#     trans[b] = i+1
# B = [trans[b] for b in B]
def cmp(A):
    cmpB = sorted(set(A))
    cmpD = { v: i+1 for i, v in enumerate(cmpB)}
    return list(map(lambda v: cmpD[v], A))
B = cmp(B)
AB = [(A[i],B[i]) for i in range(N)]
# for i in range(N):
    # AB.append((A[i],B[i]))
AB.sort()
abdict = defaultdict(list)
for i in range(N):
    abdict[AB[i][0]].append(AB[i][1])
# AB = sorted(AB,key=lambda x:x[1],reverse=True)
ans = 0
bit = BIT(N)
# for i,ab in enumerate(AB):
    # ans += i+1 - bit.query(ab[1]-1)
    # bit.update(ab[1],1)
cnt = 0
for bli in abdict.values():
    # bli = sorted(bli,reverse=True)
    cnt += len(bli)
    for b in bli:
        bit.update(b,1)
    for b in bli:
        ans += cnt - bit.query(b-1)
    # bcnt = defaultdict(int)
    # for b in bli:
    #     bcnt[b] += 1
    # for b in bcnt.keys():
    #     cnt += bcnt[b]
    #     ans += (cnt - bit.query(b-1))*bcnt[b]
    #     bit.update(b,bcnt[b])
print(ans)
