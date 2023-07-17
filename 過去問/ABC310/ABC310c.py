N = int(input())  
S = set()
for i in range(N):
  s = input()
  if s in S or s[::-1] in S:
    continue
  S.add(s)
print(len(S))