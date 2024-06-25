A, B = map(int,input().split())
if B%3 != 1 and B - A == 1:
  print('Yes')
else:
  print('No')