n=int(input())
s=input()
x=0
y=n-1
se=set()
l=[]
while y>x:
    min=10**9
    for i in range(y,-1,-1):
        if ord(s[i])<min and (ord(s[i]) not in se):
            min=ord(s[i])
    d=[]
    se.add(min)
    for i in range(y,-1,-1):
        if ord(s[i])==min:
            d.append(i)
    for z in d:
        while ord(s[x]) in se:
            x+=1
            if x>=n:
                break
        if z>x: 
            l.append([x,z])
            x+=1
            y=z
            # print(x,y)

t=list(s)
for w in l:
    a=w[0]
    b=w[1]
    tmp=t[a]
    t[a]=t[b]
    t[b]=tmp
print(''.join(t))

# ord('a')