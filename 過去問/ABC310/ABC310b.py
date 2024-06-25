N, M = map(int,input().split())
P, C, F = [], [], []
for _ in range(N):
  a = list(map(int,input().split()))
  P.append(a[0])
  C.append(a[1])
  F.append(set(a[2:]))
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    if P[i] < P[j]:
      continue
    if F[i] - F[j]:
      continue
    if P[i] > P[j] or F[j] - F[i]:
      print('Yes')
      exit()
print('No')