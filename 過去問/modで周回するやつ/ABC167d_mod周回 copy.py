N,K = map(int,input().split()) #要素数#操作回数
A = list(map(int,input().split()))
tans = [] #二週目に入るまでの答え
seen = [-1]*N #一週目に何回目の操作で要素iを訪れたか 
cycle = 0 #一周で何個の要素を訪れるか
p = 0 #次にどこの要素を訪れるか
for i in range(K+1):
    if seen[p] == -1:
        seen[p] = i
        tans.append(p+1) #i回操作したときの答え
        p = A[p] - 1    #次のpに更新
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
    m = -1
print(tans[start+m])  #sは一周するごとに答えに加算される数