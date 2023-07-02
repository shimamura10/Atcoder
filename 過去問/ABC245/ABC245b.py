N = int(input())
A = list(map(int,input().split()))
A.sort()
for i in range(2005):
    if not(i in A):
        print(i)
        break