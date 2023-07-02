a,b,c = map(int,input().split())
# [list(map(int,input().split())) for _ in range()]
# class kitai():
#     def __init__(self,a,b,c,n,p):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.n = n
#         self.p = p

P = [[[0]*100 for _ in range(100)] for _ in range(100)]
P[0][0][0] = 1
for i in range(99):
    P[i+1][0][0] = P[i][0][0]*(1 + (99-i)/(297-i))
    P[0][i+1][0] = P[0][i][0]*(1 + (99-i)/(297-i))
    P[0][0][i+1] = P[0][0][i]*(1 + (99-i)/(297-i))
    
for i in range(100):
    for j in range(100):
        for k in range(99):
            if P[i][j][k+1] == 0:
                if i+j == 198:
                    P[i][j][k+1] = P[i][j][k] + 1
                else:
                    P[i][j][k+1] = P[i][j][k]*(1 + (99-k)/(297-(i+j+k)))
                if k == 0:
                    if i < 99 and P[i+1][j][k] == 0:
                        P[i+1][j][k] = P[i][j][k]*(1 + (99-i)/(297-(i+j+k)))
                    if j < 99 and P[i][j+1][k] == 0:
                        P[i][j+1][k] = P[i][j][k]*(1 + (99-j)/(297-(i+j+k)))

print(P[:3][:3][:3])
print(P[99-a][99-b][99-c])



# l = [[[1,2],[3,1]],[[3,5],[4,2]]]
# print(l[0][0][0])

# l = [[[1]*3]*3]*3
# for i in range(2):
#     l[0][0][i+1] = 1 + l[0][0][i]
    
# print(l[2][2][2])

# l = [[0]]

# a = [0,1]
# b = [0,0]
# print(id(a[0]))
# print(id(b[0]))