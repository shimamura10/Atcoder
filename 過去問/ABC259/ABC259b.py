from math import cos, pi, sin


a,b,d = map(int,input().split())
thete = d/180*pi
ans = []
ans.append(a*cos(thete)-b*sin(thete))
ans.append(b*cos(thete)+a*sin(thete))
print(*ans)