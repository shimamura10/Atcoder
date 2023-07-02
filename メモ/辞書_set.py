from collections import defaultdict


dict = {'c':3}
#要素の追加
dict['a'] = 1
dict['b'] = 2
print(dict)   #{'c': 3, 'a': 1, 'b': 2}

#要素の削除
dict.pop('c')
print(dict)   #{'a': 1, 'b': 2}

#要素の検索(O(1)でできる！！！！！！！！)
print('a' in dict)   #True

set = set()
set.add(1)
set.discard(1)  #あれば引数に指定した要素を削除O(1)

a = {1,2,3,4,5}
b = {3,4,5,6,7}
c = a | b   #{1, 2, 3, 4, 5, 6, 7}
d = a & b   #{3, 4, 5}
print(c)
print(d)

d = defaultdict(int)  #存在しないキーを指定すると初期値を0として扱う
d['a'] += 1
print(d)

d = defaultdict(list)  #空白リスト
d['a'].append(2)
print(d)