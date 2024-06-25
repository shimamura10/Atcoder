N = int(input())
A = list(map(int,input().split()))
S = input()
Mnum = [0,0,0]
Xnum = [0,0,0]
def mex(s: set) -> int:
  for i in range(4):
    if i in s:
      continue
    return i
  return 0
for i,s in enumerate(S):
  if s == 'X':
    Xnum[A[i]] += 1
ans = 0
for i,s in enumerate(S):
  if s == 'M':
    Mnum[A[i]] += 1
  elif s == 'E':
    for m in range(3):
      for x in range(3):
        ans += mex(set([m,A[i],x])) * Mnum[m] * Xnum[x]
  elif s == 'X':
    Xnum[A[i]] -= 1
print(ans)