A,B = map(int,input().split())
def f(A,B):
    ans = []
    for i in range(A):
        ans.append(i+1)
    for i in range(B-1):
        ans.append(-(i+1))
    ans.append(-sum(ans))
    return ans
if A < B:
    ans = f(B,A)
    a = [-b for b in ans]
    print(*a)
else:
    print(*f(A,B))