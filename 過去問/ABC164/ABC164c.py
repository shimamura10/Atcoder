from collections import defaultdict
from email.policy import default


N = int(input())
s = defaultdict(int)
for i in range(N):
    S = input()
    s[S] = 0
print(len(s))