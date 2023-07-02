# class SegmentTree:
#     def __init__(self, init_val, segfunc, ide_ele):  #init_val:葉に持たせる初期値を格納したリスト
#         n = len(init_val)  #要素数
#         self.segfunc = segfunc  #子を引数とした親のノードを更新する関数
#         self.ide_ele = ide_ele  #初期値
#         self.num = 1 << (n - 1).bit_length()  #完全二分木に必要な葉の数
#         self.tree = [ide_ele] * 2 * self.num
#         self.size = n
#         for i in range(n):
#             self.tree[self.num + i] = init_val[i]
#         for i in range(self.num - 1, 0, -1):
#             self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

#     def update(self, k, x):  #k番目の要素のノードをxに更新
#         k += self.num
#         self.tree[k] = x
#         while k > 1:
#             k >>= 1
#             self.tree[k] = self.segfunc(self.tree[2*k], self.tree[2*k+1])

#     def query(self, l, r):  
#         if r==self.size:
#             r = self.num

#         res = self.ide_ele

#         l += self.num
#         r += self.num
#         right = []
#         while l < r:
#             if l & 1:
#                 res = self.segfunc(res, self.tree[l])
#                 l += 1
#             if r & 1:
#                 right.append(self.tree[r-1])
#             l >>= 1
#             r >>= 1

#         for e in right[::-1]:
#             res = self.segfunc(res,e)
#         return res

#     def bisect_l(self,l,r,x):
#         l += self.num
#         r += self.num
#         Lmin = -1
#         Rmin = -1
#         while l<r:
#             if l & 1:
#                 if self.tree[l] <= x and Lmin==-1:
#                     Lmin = l
#                 l += 1
#             if r & 1:
#                 if self.tree[r-1] <=x:
#                     Rmin = r-1
#             l >>= 1
#             r >>= 1

#         if Lmin != -1:
#             pos = Lmin
#             while pos<self.num:
#                 if self.tree[2 * pos] <=x:
#                     pos = 2 * pos
#                 else:
#                     pos = 2 * pos +1
#             return pos-self.num
#         elif Rmin != -1:
#             pos = Rmin
#             while pos<self.num:
#                 if self.tree[2 * pos] <=x:
#                     pos = 2 * pos
#                 else:
#                     pos = 2 * pos +1
#             return pos-self.num
#         else:
#             return -1

N = int(input())
A = list(map(int,input().split()))
# def segfunc(l,r):
#     res = l[0] + r[0]
#     res1 = max(res,l[1],r[1])
#     return [res,res1]
# def segfunc(l,r):
#     return l + r
# inf = -10**18
# smt = SegmentTree([[A[i],A[i]] for i in range(N)],segfunc,[0,inf])
# print(smt.tree)
# print(smt.query(1,N))
# a = [[1,2],[4,3]]
# a[0] = [2,4]
# print(a)

sum = [A[0]]
sum_max = [A[0]]
for i in range(1,N):
    sum.append(A[i] + sum[i-1])
    sum_max.append(max(sum[i],sum_max[i-1]))
ans = 0
s = 0
for i in range(N):
    ans = max(ans,s+sum_max[i])
    s += sum[i]
    # ans = max(ans,s+sum_max[i])
print(ans)
# print(sum)
# print(sum_max)