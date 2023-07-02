from heapq import heappop, heappush


Q = int(input())
ans = []
nans = []
ind = 0
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        nans.append(q[1])
    if q[0] == 2:
        if len(ans):
            print(heappop(ans))
        else:
            print(nans[ind])
            ind += 1
    if q[0] == 3:
        for i in nans[ind:]:
            heappush(ans,i)
        nans = []
        ind = 0

    