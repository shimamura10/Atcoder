def f(num,n):  #10進数のnumをn進数に直す
    res = []   #リストのi-1番目にi桁目の数字が入っていることに注意
    while num > 0:
        a = num % n
        res.append(a)
        num //= n
    return res

x = 10
print(bin(x))  #0b1010  2進数
print(oct(x))  #0o12　　8進数
print(hex(x))  #0xa　　 16進数


#n進数から10進数への変換
print(int('100', 2))
# 4
print(int('100', 3))
# 9
print(int('100', 4))
# 16
print(int('100', 8))
# 64
print(int('100', 16))
# 256