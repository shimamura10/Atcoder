N, K = map(int,input().split())
event = []
M = 0
for _ in range(N):
  a,b = map(int,input().split())
  event.append((a,b))
  M += b
event.sort()
event.reverse()
now = 0
while event:
  if M <= K:
    break
  a,b = event.pop()
  M -= b
  now = a
print(now+1)
