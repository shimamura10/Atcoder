HA, WA = map(int,input().split())
A = [input() for _ in range(HA)]
HB, WB = map(int,input().split())
B = [input() for _ in range(HB)]
HX, WX = map(int,input().split())
X = [input() for _ in range(HX)]
def cut(A, H, W):
  mi, mj, Mi, Mj = 11, 11, -1, -1
  for i in range(H):
    for j in range(W):
      if A[i][j] == '#':
        mi = min(mi, i)
        mj = min(mj, j)
        Mi = max(Mi, i)
        Mj = max(Mj, j)
  return [a[mj:Mj+1] for a in A[mi:Mi+1]]
A = cut(A, HA, WA)
B = cut(B, HB, WB)
X = cut(X, HX, WX)
nA = [[1 if s == '#' else 0 for s in a] for a in A]
nB = [[1 if s == '#' else 0 for s in a] for a in B]
nX = [[1 if s == '#' else 0 for s in a] for a in X]
def lisSum(A,B,di,dj):
  for i in range(len(B)):
    for j in range(len(B[0])):
      A[i+di][j+dj] += B[i][j]
  return A
for i in range(len(nX)-len(nA)+1):
  for j in range(len(nX[0])-len(nA[0])+1):
    for k in range(len(nX)-len(nB)+1):
      for l in range(len(nX[0])-len(nB[0])+1):
        C = [[0]*len(nX[0]) for _ in range(len(nX))]
        C = lisSum(C,nA,i,j)
        C = lisSum(C,nB,k,l)
        ok = True
        for xi in range(len(nX)):
          for xj in range(len(nX[0])):
            if nX[xi][xj] != min(1,C[xi][xj]):
              ok = False
              break
          if not ok:
            break
        if ok:
          print('Yes')
          exit()
print('No')