N = int(input())
S = input()
mod = 10**9+7
dict = {'a':0,'t':0,'c':0,'o':0,'d':0,'e':0,'r':0}
atc = ['a','t','c','o','d','e','r']
for s in S:
    if s in dict:
        ind = atc.index(s)
        if ind > 0:
            dict[s] += dict[atc[ind-1]] 
            dict[s] %= mod
        else:
            dict[s] += 1
print(dict['r']%mod)
