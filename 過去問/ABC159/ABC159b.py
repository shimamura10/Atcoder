S = input()
N = len(S)
def kb(a,b): #0-indexでaからb文字目までが回文か判断
    while a <= b:
        if S[a] != S[b]:
            return False
        a += 1
        b -= 1
    return True
if kb(0,(N-1)//2-1) and kb((N+3)//2-1,N-1) and kb(0,N-1):
    print('Yes')
else:
    print('No')