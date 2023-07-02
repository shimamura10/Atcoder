from itertools import permutations


N = int(input())
P = tuple(map(lambda x:int(x)-1,input().split()))
Q = tuple(map(lambda x:int(x)-1,input().split()))
A = list(permutations(range(N)))
a = A.index(P)
b = A.index(Q)
print(abs(a-b))
