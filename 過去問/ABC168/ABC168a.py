N = int(input())
s = [0,1,6,8]
N %= 10
if N in s:
    print('pon')
elif N == 3:
    print('bon')
else:
    print('hon')