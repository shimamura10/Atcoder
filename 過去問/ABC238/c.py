# a = []
# for i in range(17):
#     j = i
#     a.append((9*10**j*(9*10**j+1)//2))
# print(a)
# a = [0,45.0, 4095.0, 405450.0, 40504500.0, 57067588.0, 711487035.0, 232854437.0, 919067934.0, 11290336.0, 558804392.0, 266458878.0, 532155127.0, 375711423.0, 376459998.0, 706643276.0, 375405680.0, 627097645.0]
# a = [0,45, 4095, 405450, 40504500, 4050045000, 405000450000, 40500004500000, 4050000045000000, 405000000450000000, 40500000004500000000, 4050000000045000000000, 405000000000450000000000, 40500000000004500000000000, 4050000000000045000000000000, 405000000000000450000000000000, 40500000000000004500000000000000, 4050000000000000045000000000000000]
# print(len(a))
# b = []
# for i in range(18):
#     k = 0
#     for j in range(i+1):
#         k += int(a[j])
#     b.append(k)
# print(b)
# a = [0, 45, 4140, 409590, 40914090, 97981678, 809468713, 44078797, 963146731, 974437067, 534997106, 
# 801455984, 335366758, 711078181, 89293826, 795937102, 173098429, 800196074]
# a = [0, 45, 4140, 409590, 40914090, 4090959090, 409091409090, 40909095909090, 4090909140909090, 409090909590909090, 40909090914090909090, 4090909090959090909090, 409090909091409090909090, 40909090909095909090909090, 4090909090909140909090909090, 409090909090909590909090909090, 40909090909090914090909090909090, 4090909090909090959090909090909090]
a = [0, 45, 4140, 409590, 40914090, 97981678, 809468713, 44078797, 963146731, 974437067, 535000434, 
801295984, 355593574, 477994022, 452050922, 976650400, 773167328, 828456852]
strn = input()
n = int(strn)
len = len(strn)
num = n-(10**(len-1)-1)
ans = (num*(num+1)//2+a[len-1])%998244353
print(int(ans))
print(len,a[len-1])