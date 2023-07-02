N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = max(A)
s = set()
for i,a in enumerate(A):
    if M == a:
        s.add(i+1)
for b in B:
    if b in s:
        print('Yes')
        exit()
print('No')