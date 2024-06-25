N, D = map(int,input().split())
S = [input() for _ in range(N)]
ans = 0
truans = 0
for i in range(D):
  ok = True
  for s in S:
    if s[i] == 'x':
      ok = False
  if ok:
    ans += 1
  else:
    ans = 0
  truans = max(ans, truans)
print(truans)