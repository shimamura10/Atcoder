from bisect import bisect_left
from math import atan2, pi


N = int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
angle = []
for i in range(N):
    tmp = []
    x,y = xy[i]
    for j in range(N):
        if i == j:
            continue
        x2,y2 = xy[j]
        if x == x2:
            if y < y2:
                theta = 90
            else:
                theta = -90
        else:
            # a = (y2-y)/(x2-x)
            theta = atan2(y2-y,x2-x)*180/pi
        tmp.append(theta)
    tmp.sort()
    angle.append(tmp)
ans = 0
for i in range(N):
    for theta1 in angle[i]:
        theta2_ex = theta1 + 180
        if theta2_ex > 180:
            theta2_ex -= 360
        idx = bisect_left(angle[i], theta2_ex)
        for j in range(2):
            theta2 = angle[i][(idx-j)%(N-1)]
            tmp = abs(theta2-theta1)
            if tmp > 180:
                tmp = 360 - tmp
            ans = max(ans,tmp)
print(ans)