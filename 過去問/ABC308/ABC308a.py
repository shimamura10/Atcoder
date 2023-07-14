S = list(map(int,input().split()))
for i in range(len(S)):
  if i != 0 and S[i-1] > S[i]:
    print('No')
    exit()
  if S[i] < 100 or S[i] > 675 or S[i]%25 != 0:
    print('No')
    exit()
print('Yes')