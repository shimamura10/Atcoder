N,X,Y = map(int,input().split())
A = list(range(Y))
B = N - (Y-X-1)
mod = (Y-X+1)
X -= 1
Y -= 1
for k in range(1,N):
    ans = 0
    for i in range(N):
        if i > X and i + k < N:
            ans += 1
        if i <= X:
            if i + k <= X:
                ans += 1
                continue
            if i + k < Y:
                ans += 1
            if i + k + (Y-X-1) < N:
                ans += 1
        if i >= X and i <= Y and :
            i -= X
            j1 = (i+k)%mod
            j2 = (i-k)%mod
            if i < j1:
                ans += 1
            if i < j2:
                ans += 1
                if j1 == j2:
                    ans -= 1

        # j = i + k
        # if j <= X:
        #     ans += 1
        # elif i <= X:
        #     if j < Y:
        #         ans += 1
        #     if j < B:
        #         ans += 1
        # elif i > X and j < N:
        #     ans += 1
    print(ans)
