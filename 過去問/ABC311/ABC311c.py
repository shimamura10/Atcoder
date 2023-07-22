N = int(input())
A = list(map(int,input().split()))
seen = [False]*N
now = 0
seen[0] = True
while True:
  nex = A[now] - 1
  if seen[nex]:
    ans = [nex]
    start = nex
    while True:
      nex = A[nex] - 1
      if nex == start:
        print(len(ans))
        print(*[a+1 for a in ans])
        exit()
      ans.append(nex)
  seen[nex] = True
  now = nex