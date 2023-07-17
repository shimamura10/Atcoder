N, T, M = map(int,input().split())
badPairs = [list(map(lambda x: int(x)-1,input().split())) for _ in range(M)]
ans = 0

tmp = 1
for i in range(10):
  tmp *= i+1
print(tmp)