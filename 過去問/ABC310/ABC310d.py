N, T, M = map(int,input().split())
badPairs = [set() for _ in range(N)]
for _ in range(M):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  badPairs[a].add(b)
  badPairs[b].add(a)
ans = 0
# Groups: list[set] = []
Groups = []

def dfs(i):
  if i == N:
    global ans
    ans += 1
    return
  if len(Groups) < T:
    Groups.append(set([i]))
    dfs(i+1)
    del Groups[-1]
  if T - len(Groups) >= N-i:
    return
  for g in Groups:
    if g & badPairs[i]:
      continue
    g.add(i)
    dfs(i+1)
    g.discard(i)
  return
dfs(0)
print(ans)