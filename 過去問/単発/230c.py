N,A,B = map(int,input().split())
P,Q,R,S = map(int,input().split())
k_min1 = max(1-A,1-B)
k_max1 = min(N-A,N-B)
k_min2 = max(1-A,B-N)
k_max2 = min(N-A,B-1)
ans = [['.']*(S-R+1) for i in range(Q-R+1)]
x1 = max(A+k_min1,P)
x2 = min(A+k_max1,Q)
for i in range(x1,x2+1):
    j = i + B - A
    if j < R or j > S:
        continue
    ans[i-P][j-R] = '#'

x3 = max(A+k_min2,P)
x4 = min(A+k_max2,Q)
for i in range(x3,x4+1):
    j = -i + A + B
    if j < R or j > S:
        continue
    ans[i-P][j-R] = '#'

for i in range(Q-P+1):
    print(''.join(ans[i]))

# for i in range(Q-P+1):
#     a = ''
#     for j in range(S-R+1):
#         if ans[i][j]:
#             a += '#'
#         else:
#             a += '.'
#     print(a)

import time
a = 10**18
b = 10**18-1
t1 = time.time()
print(max(a,b))
t2 = time.time()
print(t2-t1)
# ans = ['.'*(5) for i in range(4)]
# ans[3] = ans[3][:2] + '#' + ans[3][3:]
# print(ans[3])