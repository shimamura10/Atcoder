N = int(input())
W = list(map(int,input().split()))
B = list(map(int,input().split()))
maxb = 50*51//2 + 50
Grundy_num = [[-1]*(maxb+1) for _ in range(51)]
# https://algo-logic.info/combinatorial-games/
for w in range(51):
    for b in range(maxb+1):
        tmp = set()
        if w > 0 and (b + w) <= maxb:
            tmp.add(Grundy_num[w-1][b+w])
        for k in range(b//2):
            k += 1
            tmp.add(Grundy_num[w][b-k])
        for g in range(maxb):
            if not g in tmp:
                Grundy_num[w][b] = g
                break
xor = 0
for i in range(N):
    xor ^= Grundy_num[W[i]][B[i]]
if xor == 0:
    print("Second")
else:
    print("First")