N = int(input())
A = list(map(int,input().split()))
dpsil = [0]*(N+1)
dpgol = [0]*(N+1)
dpgol[0] = 1
for i in range(N):
    dpsil[i+1] = max(dpsil[i],dpgol[i]*A[i])
    dpgol[i+1] = max(dpgol[i],dpsil[i]/A[i])
ans = []
max = dpgol[-1]
gold = True
for i in reversed(range(N)):
    if gold:
        if max == dpgol[i]:
            ans.append(0)
        else:
            ans.append(1)
            max = dpsil[i]
            gold = False
    else:
        if max == dpsil[i]:
            ans.append(0)
        else:
            ans.append(1)
            max = dpgol[i]
            gold = True
print(*ans[::-1])