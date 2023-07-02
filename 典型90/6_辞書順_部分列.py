from bisect import bisect_left, bisect_right


N,K = map(int,input().split())
S = input()
d = {}
for i,s in enumerate(S):
    if not(ord(s) in d):
        d[ord(s)] = [i]
    else:
        d[ord(s)].append(i)
ans = ''
ind = -1
for n in range(K):
    for i in range(ord('a'),ord('z')+1):
        if i in d:
            tmp = bisect_right(d[i],ind)
            if tmp < len(d[i]) and N - d[i][tmp] >= K - n:
                ans += chr(i)
                ind = d[i][tmp]
                break
print(''.join(ans))

