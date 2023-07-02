from collections import deque


H,W = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
s = [input() for _ in range(H)]
inf = H*W
d = [[inf]*W for _ in range(H)]
q = deque(maxlen = inf)
q.append((sx-1,sy-1))
idx = 1
k = 0
nexti = 0
seen = [[False]*W for _ in range(H)]
count = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            d[i][j] = -10
while len(q):
    print(q)
    x,y = q.popleft()
    if count == inf:
        break
    idx -= 1
    # if d[x][y] == -1:
    #     d[x][y] = k
    
    i = x + 1
    j = y
    while 0 <= i and i < H and 0 <= j and j < W:
        if d[i][j] < k - 1:
            break
        
        if d[i][j] == inf:
            q.append((i,j))
            d[i][j] = k
            # seen[i][j] = True
            nexti += 1
            count += 1
            if count == inf or (i == gx-1 and j == gy-1):
                print(d[gx-1][gy-1])
                exit()
        i += 1
    i = x - 1
    j = y
    while 0 <= i and i < H and 0 <= j and j < W:
        if d[i][j] < k - 1:
            break
        if d[i][j] == inf:
            q.append((i,j))
            d[i][j] = k
            # seen[i][j] = True
            nexti += 1
            count += 1
            if count == inf or (i == gx-1 and j == gy-1):
                print(d[gx-1][gy-1])
                exit()
        i -= 1
    i = x 
    j = y + 1
    while 0 <= i and i < H and 0 <= j and j < W:
        if d[i][j] < k - 1:
            break
        if d[i][j] == inf:
            q.append((i,j))
            d[i][j] = k
            # seen[i][j] = True
            nexti += 1
            count += 1
            if count == inf or (i == gx-1 and j == gy-1):
                print(d[gx-1][gy-1])
                exit()
        j += 1
    i = x
    j = y - 1
    while 0 <= i and i < H and 0 <= j and j < W:
        if d[i][j] < k - 1:
            break
        if d[i][j] == inf:
            q.append((i,j))
            d[i][j] = k
            # seen[i][j] = True
            nexti += 1
            count += 1
            if count == inf or (i == gx-1 and j == gy-1):
                print(d[gx-1][gy-1])
                exit()
        j -= 1

    if idx == 0:
        k += 1
        idx = nexti
        nexti = 0
print(d[gx-1][gy-1])
# print(d)