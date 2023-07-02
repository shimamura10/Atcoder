# N = 10**5 #要素数
# K = 10**18 #操作回数
from itertools import accumulate


K,X,N = map(int,input().split())
tans = [0] #二週目に入るまでの答え
seen = [-1]*N #一週目に何回目の操作で要素iを訪れたか 
cycle = 0 #一周で何個の要素を訪れるか
p = X #次にどこの要素を訪れるか
m = 0
n = 0
for i in range(K):
    if seen[p] == -1:
        seen[p] = i
        tans.append(p) #i回操作したときの答え
        p = (p**2)%N     #次のpに更新
    else:
        cycle = i - seen[p]
        m = (K-seen[p])%cycle
        n = (K-seen[p])//cycle
        break
tans = list(accumulate(tans))
start = len(tans) - cycle #tans[start]から周回が始まる

# if cycle > 0:
#     m = (K-start)%cycle #周回の何個目で操作が終わるか
#     n = (K-start)//cycle #何週するか
# else:
#     start -= 1
s = tans[-1] - tans[start]
print(tans[start+m]+s*n)  #sは一周するごとに答えに加算される数