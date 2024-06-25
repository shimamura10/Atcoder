N = int(input())
S = input()
num_1 = 0
ans = 0
for i,s in enumerate(S):
  if s == '0':
    num_1 = i
  elif s == '1':
    num_1 = 1 + i - num_1
  ans += num_1
print(ans)