N = int(input())
A = list(map(int,input().split()))
seen = [[] for i in range(200)]
seen[0] = [0]
for i in range(N):
    for j in range(200):
        if len(seen[j]) != 0 and seen[j][-1] != i+1:
            if len(seen[(j+A[i])%200]) < 2:
                seen[(j+A[i])%200] = seen[j] + [i+1]
            else:
                B = seen[(j+A[i])%200]
                seen[j].append(i+1)
                C = seen[j]
                B[0] = len(B) - 1
                C[0] = len(C) - 1
                print('Yes')
                print(*B)
                print(*C)
                exit()
print('No')