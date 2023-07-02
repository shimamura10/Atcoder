N,K = map(int,input().split())
A = list(map(int,input().split()))
seen = [-1]*N
vis = []
p = 0
n = 0
for i in range(K):
    if seen[p] == -1:
        seen[p] = i
        vis.append(p)
        p = A[p] - 1
    else:
        n = i - seen[p]
        break
start = len(vis) - n
vis.append(p)
if n == 0:
    mod = 0
else: 
    mod = (K-start)%n
print(vis[start+mod]+1)