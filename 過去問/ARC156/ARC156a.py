T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    s = 0
    for n in S:
        s += int(n)
    if s%2:
        print(-1)
        continue
    ans = -1
    if S == "0110":
        ans = 3
    elif N == 3:
        if S[1] == '0':
            ans = s//2
    elif s == 2:
        idx1 = 0
        idx2 = 0
        ok1 = True
        for i in range(N):
            if ok1 and S[i] == '1':
                idx1 = i
                ok1 = False
            elif S[i] == '1':
                idx2 = i
        if idx2-idx1 == 1:
            ans = 2
        else:
            ans = s//2
    else:
        ans = s//2
    print(ans)
    