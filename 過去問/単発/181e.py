import bisect
# a = [1,3,6,7]
# print(bisect.bisect_left(a,5))
N,M = map(int,input().split())
H = list(map(int,input().split()))
W = list(map(int,input().split()))
H.sort()
a = [0]
b = [0]
pa = 0
pb = 0
for i in range(N//2):
    a.append(H[2*i+1]-H[2*i]+pa)
    b.append(H[-(2*i+1)]-H[-(2*i+2)]+pb)
    pa = a[-1]
    pb = b[-1]
ans = 10**9
for j in range(M):
    i = bisect.bisect_left(H,W[j])
    ans = min(ans,a[i//2]+abs(H[i-(i%2)]-W[j])+b[N//2-i//2])
print(ans)