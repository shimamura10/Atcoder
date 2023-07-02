from collections import defaultdict


N = int(input())
A = list(map(int,input().split()))
M = max(A)
cnt = defaultdict(int)
for a in A:
    cnt[a] += 1
seen = defaultdict(int)
li = list(cnt.keys())
# for k in cnt.keys():
#     li.append(k)
li.sort()
for key in li:
    for k in li:
        if k*key > M:
            break
        # if k == 1:
        #     continue
        # if k == key:
        #     seen[k**2] += cnt[k]**2
        # else:
        #     seen[k*key] += cnt[k]*cnt[key]
        seen[k*key] += cnt[k]*cnt[key]
ans = 0
for a in A:
    ans += seen[a]
    # if a != 1:
    #     ans += cnt[1]*(cnt[a]-1)*2
# ans += cnt[1]**3
print(ans)

# for i in range(N):
#     tmp = 0
#     mytmp = seen[A[i]]
#     # mytmp += cnt[1]*(cnt[A[i]]-1)*2
#     for j in range(N):
#         for k in range(N):
#             if A[i] == A[j]*A[k]:
#                 tmp += 1