S = input()
Q = int(input())
abc = ['A','B','C']
for _ in range(Q):
    t,k = map(int,input().split())
    k -= 1
    cnt = 0
    for i in range(t):
        if k%2:
            cnt -= 1
        else:
            cnt += 1
        k //= 2
        if k == 0:
            cnt += t - (i+1)
            break
    print(abc[(abc.index(S[k])+cnt)%3])