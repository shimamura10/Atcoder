N = int(input())
S = [input() for _ in range(N)]
ans = 'No'
for i in range(N-5):
    for j in range(N):
        x = 0
        for k in range(6):
            if S[i+k][j] == '.':
                x += 1
        if x <= 2:
            ans = 'Yes'
for i in range(N):
    for j in range(N-5):
        y = 0
        for k in range(6):
            if S[i][j+k] == '.':
                y += 1
        if y <= 2:
            ans = 'Yes'
for i in range(N-5):
    for j in range(N-5):
        z = 0
        for k in range(6):
            if S[i+k][j+k] == '.':
                z += 1
        if z <= 2:
            ans = 'Yes'
for i in range(N-1,4,-1):
    for j in range(N-5):
        w = 0
        for k in range(6):
            if S[i-k][j+k] == '.':
                w += 1
        if w <= 2:
            ans = 'Yes'
            break
print(ans)
    