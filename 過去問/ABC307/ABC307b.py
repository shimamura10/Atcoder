def kb(a,b,S): #0-indexでaからb文字目までが回文か判断
    while a <= b:
        if S[a] != S[b]:
            return False
        a += 1
        b -= 1
    return True
N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i == j:
      continue
    if kb(0,len(S[i]+S[j])-1,S[i]+S[j]):
      print('Yes')
      exit()
print('No')
