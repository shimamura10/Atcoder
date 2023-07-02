from bisect import bisect_right


N,K = map(int,input().split())
A = list(map(int,input().split()))
B = [A[K-1]]
for k in reversed(range(K-1)):
    B.append(min(B[-1],A[k]))
B = B[::-1]
ans = 10**7
for i in range(K,N):
    if B[0] >= A[i]:
        continue
    ind = bisect_right(B,A[i]-1)
    tmp = i - ind + 1
    ans = min(ans,tmp)
if ans == 10**7:
    print(-1)
else:
    print(ans)

