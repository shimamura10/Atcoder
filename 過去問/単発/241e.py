

n,k = map(int,input().split())
A = list(map(int,input().split()))
seen = [-1]*n
ind = 0
sum = [0]
i = 0
while seen[i] == -1 and ind < k:
    sum.append(sum[-1]+A[i])
    seen[i] = ind
    i = (i+A[i])%n
    ind += 1
k -= seen[i]
p = k//(ind - seen[i])
q = k%(ind - seen[i])
ans = (sum[-1]-sum[seen[i]])*p + sum[q+seen[i]]
# print(i)
# print(sum,p,q)
print(ans)
# print(seen)