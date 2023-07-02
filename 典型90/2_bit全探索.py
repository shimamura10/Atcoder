N = int(input())
if N%2 == 1:
    exit()

for bit in range(1<<N):
    ans = []
    a,b = 0,0
    ok = True
    for i in reversed(range(N)):
        if bit>>i & 1:
            b += 1
            ans+= ')'
        else:
            a += 1
            ans += '('
        if a < b or a > N//2 or b > N//2:
            ok = False
            break
    if ok:
        print(''.join(ans))
