N = 10**5 #要素数
K = 10**18 #操作回数
tans = [] #二週目に入るまでの答え
seen = [-1]*N #一週目に何回目の操作で要素iを訪れたか 
cycle = 0 #一周で何個の要素を訪れるか
p = 0 #次にどこの要素を訪れるか
for i in range(K+1):
    if seen[p] == -1:
        seen[p] = i
        tans.append( ) #i回操作したときの答え
        p =      #次のpに更新
    else:
        cycle = i - seen[p]
        break
start = len(tans) - cycle #tans[start]から周回が始まる
m = 0
n = 0
if cycle > 0:
    m = (K-start)%cycle #周回の何個目で操作が終わるか
    n = (K-start)//cycle #何週するか
else:
    start -= 1
print(tans[start+m]+s*n)  #sは一周するごとに答えに加算される数