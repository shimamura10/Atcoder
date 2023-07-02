h1,h2,h3,w1,w2,w3 = map(int,input().split())
ans = [[0,0,0] for i in range(3)]
cnt = 0
for a in range(1,31):
    for b in range(1,31):
        for c in range(1,31):
            for d in range(1,31):
                if h1 - a- b <= 0:
                    continue
                if h2 - c - d <= 0:
                    continue
                if w1 - a - c <= 0:
                    continue
                if w2 - b - d <= 0:
                    continue
                if w3 - (h1 - a- b) - (h2 - c - d) <= 0:
                    continue
                if h3 - (w1 - a - c) - (w2 - b - d) <= 0:
                    continue
                if w3 - (h1 - a- b) - (h2 - c - d) != h3 - (w1 - a - c) - (w2 - b - d):
                    continue
                cnt += 1
print(cnt)