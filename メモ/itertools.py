#累積和
from collections import defaultdict
import itertools
ary = [1, 3, 5, 7, 9]
cumsum = itertools.accumulate(ary)
print(list(cumsum))
# -> [1, 4, 9, 16, 25]
s = ['ab', 'bc', 'cd']
print(list(itertools.accumulate(s)))
# -> ['ab', 'abbc', 'abbccd']

#同じ値をグループ化
bi = [0,0,0,1,1,0,0,0,1,1,0,1]
gr = itertools.groupby(bi)
groups = []
keys = []
for key, group in gr:
    print(f'{key}: {list(group)}')
    groups.append(list(group))
    keys.append(key)
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0, 0, 0]
# 1: [1, 1]
# 0: [0]
# 1: [1]

#順列
print(list(itertools.permutations([1, 2, 3])))
# -> [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# print(list(itertools.permutations('Qiita')))
# ->文字列も可
print(list(itertools.permutations([3,1,1,2])))

#組み合わせ
print(list(itertools.combinations([1, 2, 3], 2)))
# -> [(1, 2), (1, 3), (2, 3)]
print(list(itertools.combinations_with_replacement([1, 2, 3], 2)))
# -> [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
print(list(itertools.product([0,1], repeat=3)))
# -> [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

#インデックスとリストの中身を取得
l = ['a','b','c']
print(list(enumerate(l)))  #[(0, 'a'), (1, 'b'), (2, 'c')]