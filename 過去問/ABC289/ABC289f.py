sx,sy = map(int,input().split())
tx,ty = map(int,input().split())
a,b,c,d = map(int,input().split())
if (sx-sy)%2 or (tx-ty)%2:
    print("No")
    exit()
if (a == b and sx != tx) or (c == d and sy != ty):
    print("No") 
    exit()
if a <= tx and tx <= b:
    while sx != tx:
        m = (sx-tx)//2