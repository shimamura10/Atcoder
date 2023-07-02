r,c = map(lambda x:int(x)-1,input().split())
A = [list(map(int,input().split())) for _ in range(2)]
print(A[r][c])