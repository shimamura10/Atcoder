sx,sy,gx,gy = map(int,input().split())
gy *= -1
a = (gy-sy)/(gx-sx)
ans = sx-sy/a
print(ans)