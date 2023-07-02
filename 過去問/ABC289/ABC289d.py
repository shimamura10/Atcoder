N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
X = int(input())
rad = [0]*(X+1)
for b in B:
    rad[b] = -1
rad[0] = 1
for i in range(X+1):
    if rad[i] <= 0:
        continue
    for a in A:
        if a + i <= X and rad[a+i] >= 0:
            rad[a+i] = 1
if rad[X] == 1:
    print("Yes") 
else:
    print("No")