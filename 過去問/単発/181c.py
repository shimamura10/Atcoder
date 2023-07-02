N = int(input())
# x = [0]*3000
# y = [0]*3000
# for i in range(N):
#     a,b = map(int,input().split())
#     x[a] += 1
#     y[b] += 1
#     if x[a] >= 3 or y[b] >= 3:
#         print('Yes')
#         exit()
# print('No')
p = [list(map(int,input().split())) for _ in range(N)]
# a,b = p[0]
# print(a,b)
for i in range(N):
    x1,y1 = p[i][0],p[i][1]
    for j in range(i+1,N):
        # if j == i:
        #     continue
        # a = 0
        # b = 0
        # c = 0
        # d = 0
        x2,y2 = p[j][0],p[j][1]
        # if x2 == x1:
        #     a += 1
        # if y2 == y1:
        #     b += 1
        # if x2 - x1 == y2 - y1:
        #     c += 1
        # if x2 - x1 == y1 - y2:
        #     d += 1
        if x2 != x1:
            a = (y2-y1)/(x2-x1)
        else:
            a = 10*4
        for k in range(j+1,N):
            # if k == j or k == i:
            #     continue
            x3,y3 = p[k][0],p[k][1]
            # if x3 == x1:
            #     a += 1
            # if y3 == y1:
            #     b += 1
            # if x3 - x1 == y3 - y1:
            #     c += 1
            # if x3 - x1 == y1 - y3:
            #     d += 1
            # if a == 2 or b == 2 or c == 2 or d == 2:
            if x3 != x1:
                if a == (y3-y1)/(x3-x1):
                    print('Yes')
                    # print(i,j,k,a,b,c,d)
                    exit()
            else:
                if a == 10*4:
                    print('Yes')
                    exit()
print('No')
    


