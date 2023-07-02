N,A,B = list(map(int,input().split()))
w = '.'*B
b = '#'*B
for i in range(N):
    for j in range(A):
        ans = ''
        for k in range(N):
            if (i+k)%2:
                ans += b
            else:
                ans += w
        print(ans)
