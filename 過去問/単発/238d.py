T = int(input())
A = [list(map(int,input().split())) for i in range(T)]
def f(x):
    ans = []
    while x >1:
        ans.append(x%2)
        x //= 2
    ans.append(x)
    return ans

for i in range(T):
    a = A[i][0]
    s = A[i][1]
    b = s - 2*a
    if b < 0:
        print('No')
        continue
    else:
        a_2 = f(a)
        b_2 = f(b)
        na = len(a_2)
        nb = len(b_2)
        if na < nb:
            n = na
        else:
            n = nb
        ans = 'Yes'
        for j in range(n):
            if a_2[j] == 1 and b_2[j] == 1:
                ans = 'No'
                break
        print(ans)

