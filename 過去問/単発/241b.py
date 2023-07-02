N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort()
import bisect
ans = 'Yes'
for i in range(M):
    if B[i] in A:
        del A[A.index(B[i])]
    else:
        ans = 'No'
        break
print(ans)
# import bisect
# a = [1,4]
# print(bisect.bisect_left(a,5))