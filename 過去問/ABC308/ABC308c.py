N = int(input())
AB = []
for i in range(N):
  a,b = map(int,input().split())
  AB.append((a,a+b))

def quicksort(A: list, cmpfn):
  print(type(cmpfn))
  if len(A) == 0:
    return []
  p = sorted([A[0], A[-1], A[len(A)//2]])[1]
  left, equal, right = [], [], []
  for a in A:
    if cmpfn(a,p) == 0:
      equal.append(a)
    elif cmpfn(a,p) == -1:
      left.append(a)
    elif cmpfn(a,p) == 1:
      right.append(a)
  return quicksort(left, cmpfn) + equal + quicksort(right, cmpfn)

def cmpfn(a,b):
  dif = AB[a][0]*AB[b][1] - AB[b][0]*AB[a][1]
  if dif == 0:
    return 0
  elif dif < 0:
    return -1
  elif dif > 0:
    return 1
ans = quicksort([i for i in range(N)], cmpfn)
print(*[a+1 for a in ans])