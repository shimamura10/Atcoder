#SとS[i:]の最長共通接頭辞(LCP)の長さをリストにして返す
def Z_algo(S):   #O(n)
    n = len(S)
    LCP = [0]*n
    i = 1
    j = 0
    c = 0#最も末尾側までLCPを求めたインデックス
    for i in range(1, n):
        #i番目からのLCPが以前計算したcからのLCPに含まれている場合
        if i+LCP[i-c] < c+LCP[c]:
            LCP[i] = LCP[i-c]
        else:
            j = max(0, c+LCP[c]-i)
            while i+j < n and S[j] == S[i+j]: j+=1
            LCP[i] = j
            c = i
    LCP[0] = n
    return LCP
s = 'momomosumomomomo'
print(Z_algo(s))

def my_Z_algo(S):   #O(n)
    n = len(S)
    LCP = [0]*n
    i = 1
    j = 0
    c = 0#最も末尾側までLCPを求めたインデックス
    while i < n:
        while i + j < n and S[j] == S[i+j]: j += 1
        LCP[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while k < j and k + LCP[k] < j:
            LCP[i+k] = LCP[k]
            k += 1
        i += k
        j -= k
    return LCP
S = "momomosumomomomo"
print(my_Z_algo(S))