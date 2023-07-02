from itertools import accumulate


X = input()
S = [ int(i) for i in X]
S = list(accumulate(S))
ans = ''
up = 0
for i in range(len(X)):
    up += S[-(i+1)]
    ans += str(up%10)
    up //= 10
while up > 0:
    ans += str(up%10)
    up //= 10
ans = ans[::-1]
print(''.join(ans))