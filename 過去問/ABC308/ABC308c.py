N = int(input())
L = []
for i in range(N):
  a,b = map(int,input().split())
  L.append((a/(a+b),i+1))
L.sort(key=lambda x:x[1])
L.sort(key=lambda x:x[0], reverse=True)
print(*[l[1] for l in L])