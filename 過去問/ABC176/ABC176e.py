H,W,M = map(int,input().split())
numi = [0]*H
numj = [0]*W
bomb = set()
for _ in range(M):
    h,w = map(int,input().split())
    bomb.add((h,w))
    h -= 1
    w -= 1
    numi[h] += 1
    numj[w] += 1
maxi = max(numi)
maxj = max(numj)

numi1 = []
numj1 = []
for i in range(H):
    if numi[i] == maxi:
        numi1.append(i+1)
for i in range(W):
    if numj[i] == maxj:
        numj1.append(i+1)
if len(numi1)*len(numj1) > M:
    print(maxi+maxj)
    exit()
for i in numi1:
    for j in numj1:
        if (i,j) in bomb:
            continue
        print(maxi+maxj)
        exit()
print(maxi+maxj-1)

