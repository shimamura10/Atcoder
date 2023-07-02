import collections
N,M = map(int,input().split())
kyoutyo = []
kyoutyo_num = [[] for _ in range(N)]
for i in range(M):
    k = int(input())
    R = list(map(lambda x:int(x)-1,input().split()))
    kyoutyo.append(R)
    for r in R:
        kyoutyo_num[r].append(i)
ans = [-1]*N
q = collections.deque()
q.append(0)
seen = [False]*M
ans[0] = 0
while q:
    n = q.popleft()
    for i in kyoutyo_num[n]:
        if not seen[i]:
            for r in kyoutyo[i]:
                if ans[r] == -1:
                    q.append(r)
                    ans[r] = ans[n]+1
            seen[i] = True
for a in ans:
    print(a)