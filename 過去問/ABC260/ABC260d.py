from bisect import bisect_left


N,K = map(int,input().split())
P = list(map(int,input().split()))
omote = [0]
yama = []
ans = [-1]*N
next = [-1]*(N+2)
def ditect(ind):
    nind = ind
    while next[nind] > 0:
        nind = next[nind]
    next[ind] = nind
    return nind
for i,p in enumerate(P):
    ind = bisect_left(omote,p)
    if ind == len(omote):
        omote.append(p)
        yama.append([p])
    else:
        # if next[ind] >= 0:
        #     ind = ditect(ind)
        omote[ind] = p
        yama[ind-1].append(p)
    if len(yama[ind-1]) == K:
        for p in yama[ind-1]:
            ans[p-1] = i + 1
        del omote[ind]
        del yama[ind-1]
        # if next[ind+1] > 0:
        #     nind = ditect(ind+1)
        #     next[ind] = nind
        # else:
        #     next[ind] = ind + 1
for a in ans:
    print(a)