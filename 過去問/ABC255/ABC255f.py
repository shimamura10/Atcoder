N = int(input())
P = list(map(lambda x:int(x)-1,input().split()))
I = list(map(lambda x:int(x)-1,input().split()))

ans = [[0,0,0] for i in range(N)]
seen = set()
np = 0
ni = 0
tmp = 0
ok = True
for i,p in enumerate(P):
    if p in seen:
        continue
    if p == I[ni]:
        ans[P[i-1]][0] = p
        ans[p][2] = P[i-1]
        seen.add(p)
        ni += 1
        tmp = p
        while I[ni] in seen:
            tmp = ans[tmp][2]
            if I[ni] != tmp:
                print(-1)
                exit()
            ni += 1
        ans[tmp][1] = P[i+1]
        seen.add(P[i+1])
        # while ans[tmp][2] == I[ni]:
        #     tmp = ans[tmp][2]
        #     ni += 1  
    else:
        ans[P[i-1]][0] = p
        ans[p][2] = P[i-1]
        seen.add(p)

while True:
    if P[np] == I[ni]:
        ans[tmp][0] = P[np]
        ans[P[np]][2] = tmp
        tmp = P[np]
        seen.add(P[np])
        ni += 1
        np += 1
        while I[ni] in seen:
            tmp = ans[tmp][2]
            if I[ni] != tmp:
                print(-1)
                exit()
            ni += 1
        ans[tmp][1] = P[np]
        ans[P[np]][2] = tmp
        tmp = P[np]
        seen.add(P[np])
        np += 1
        