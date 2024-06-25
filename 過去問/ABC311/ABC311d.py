N,M = map(int,input().split())
S = [input() for _ in range(N)]
stack = [[1,1]]
seen = [[False]*M for _ in range(N)]
di = [0,0,1,-1]
dj = [1,-1,0,0]
while stack:
  i,j = stack.pop()
  for d in range(4):
    ti = i
    tj = j
    ni = i
    tj = j
    while True:
      ni = ti+di[d]
      nj = tj+dj[d]
      if S[ni][nj] == '#':
        if seen[ti][tj] == False:
          stack.append([ti,tj])
          seen[ti][tj] = True
        break
      seen[ti][tj] = True
      ti = ni
      tj = nj
    # if seen[ni][nj] or S[ni][nj] == '#':
    #   continue
    # seen[ni][nj] = True
    # stack.append([ni,nj])
print(sum([sum(s) for s in seen]))