# def 名前(引数, 引数, ...):
#     return 式

# 名前 = lambda 引数, 引数, ...: 式
lambda a,b : a+b

#二個目の要素でソート
l = [[1,4],[2,7],[6,1]]
l = sorted(l,key= lambda x:x[1])
print(l)

# if文を使う
lambda x: 'even' if x%2 == 0 else 'odd'

l = [1,3,4,7,4,9,0]
s = sum(1 for x in l if x %2 == 0)
print(s)

A = [[1,2,3],[4,5,6],[7,8,9]]
print(sum(a[1] for a in A))