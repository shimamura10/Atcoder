from bisect import bisect_left


N = int(input())
A = list(map(int,input().split()))
RA = A[::-1]
inf = float('inf')
dp1 = [inf]*N
a = []   #a[i]はA[i]を末尾にもつ最長増加部分列の長さ
b = []
dp2 = [inf]*N
for i in range(N):
    idx = bisect_left(dp1,A[i])
    dp1[idx] = A[i]
    a.append(idx+1)
    idx = bisect_left(dp2,RA[i])
    dp2[idx] = RA[i]
    b.append(idx+1)
ans = 0
for i in range(N):  #Bkについて全探索
    ans = max(a[i]+b[-(i+1)]-1,ans)
print(ans)