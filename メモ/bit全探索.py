#リストの部分集合の全探索ができる

a = [3,1,2]
n = len(a)
ans = []
for bit in range(1<<n):
    s = []
    for j in range(n):
        if bit & 1<<j:
            s.append(a[j])
    ans.append(s)
print(ans)

# 求める要素数は2^n(=1<<n)であり、
# bitを二進数にしたとき1になっている要素を選択することで、
# リストの部分集合を全列挙している