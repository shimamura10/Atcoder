from collections import deque


N,K = map(int,input().split())
a = list(map(int,input().split()))
s = set()
for i in range(N):
    s.add(a[i])
dict = {}
while len(s) != 0:
    dict[s.pop()] = deque()
k = 0
ans = 0
pa = -1
que = deque()
d = 0
for i in range(N):
    if pa != a[i]:
        que.append(a[i])
        dict[a[i]].append(1)
        if len(dict[a[i]]) == 1:
            k += 1
        while k > K:
            b = que.popleft()
            d += dict[b].popleft()
            if len(dict[b]) == 0:
                k -= 1
    else:
        dict[a[i]][-1] += 1
    ans = max(ans,i+1-d)
print(ans)
# print(d)

# from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d[-1] += 1
# print(d)
# dict = {}
# dict['a'] = deque()
# dict['a'].append(1)
# print(dict['a'].popleft())
# print(type(dict['a']))