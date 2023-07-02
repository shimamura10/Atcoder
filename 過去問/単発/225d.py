N,Q = map(int,input().split())
a = [[0,0] for _ in range(N+1)]
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x = q[1]
        y = q[2]
        a[x][1] = y
        a[y][0] = x
    elif q[0] == 2:
        x = q[1]
        y = q[2]
        a[x][1] = 0
        a[y][0] = 0
    elif q[0] == 3:
        x = q[1]
        ans_l = []
        ans_r = []
        j = a[x][0]
        M = 1
        while j > 0:
            ans_l.append(j)
            j = a[j][0]
            M += 1
        k = a[x][1]
        while k > 0:
            ans_r.append(k)
            k = a[k][1]
            M += 1
        print(M,*(ans_l[::-1]+[x]+ans_r))