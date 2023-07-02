#N以下の約数の個数のリストを作る
N = 20
d = [0]*(N+1)
for i in range(1,N+1):
    j = 1
    while i * j <= N:
        d[i*j] += 1
        j += 1
print(d) 
# ΣN/k ~ NlogN なので)(NlogN)でできる
