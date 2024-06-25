N = int(input())
S = input()
ok = [0,0,0]
for i,s in enumerate(S):
  if s == 'A':
    ok[0] = 1
  elif s == 'B':
    ok[1] = 1
  elif s == 'C':
    ok[2] = 1
  if sum(ok) == 3:
    print(i+1)
    break
