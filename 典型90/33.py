H,W = map(int,input().split())
seen = [[-1]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if seen[i][j] == -1:
            seen[i][j] = 1
            if i < H - 1:
                seen[i+1][j] = 0
            if j < W - 1:
                seen[i][j+1] = 0
            if i < H - 1 and j < W - 1:
                seen[i+1][j+1] = 0
ans = 0
for i in range(H):
    ans += sum(seen[i])
if H == 1:
    ans = W
if W == 1:
    ans = H
print(ans)
        