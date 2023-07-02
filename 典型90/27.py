N = int(input())
seen = set()
for i in range(N):
    s = input()
    if s in seen:
        continue
    seen.add(s)
    print(i+1)