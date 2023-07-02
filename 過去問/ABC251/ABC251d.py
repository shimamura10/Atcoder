W = int(input())
seen = [False]*(W+1)
ans = []
seen2 = set()
for i in range(1,W+1):
    if seen[i]:
        continue
    seen[i] = True
    for a in seen2:
        if a + i <= W:
            seen[a+i] = True
    for a in ans:
        if a + i <= W:
            seen2.add(a+i)
            seen[a+i] = True
    # for j in range(len(ans)):
    #     a = ans[j] + i
    #     if a <= W:
    #         seen[a] = True 
    #     for k in range(j):
    #         a = ans[j] + ans[k] + i
    #         if a <= W:
    #             seen[a] = True
    ans.append(i)
print(len(ans))
print(*ans)