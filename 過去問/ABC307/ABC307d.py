N = int(input())
S = input()
cut = []
cntleft = []
right = 0
for i,s in enumerate(S):
  if s == '(':
    cntleft.append(i)
  elif s == ')':
    if cntleft:
      left = cntleft.pop()
      right = i
      cut.append((left,right))
cut.sort()
exist = [True]*N
for c in cut:
  l,r = c
  for i in range(l,r+1):
    if exist[i] == False:
      break
    exist[i] = False
ans = []
for i,s in enumerate(S):
  if exist[i]:
    ans.append(S[i]) 
print(''.join(ans))