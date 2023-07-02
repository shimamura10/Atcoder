K = int(input())
a = 0
for i in range(K):
    a = (a*10 + 7)%K
    if a == 0:
        print(i+1)
        exit()
print(-1)