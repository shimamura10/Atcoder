x1,y1,x2,y2 = map(int,input().split())
x = abs(x2 - x1)
y = abs(y2 - y1)
p = [x,y]
# print(p)
A = [[2,0],[4,0],[1,1],[3,1],[0,2],[4,2],[1,3],[3,3],[0,4],[2,4]]
ans = 'No'
for i in range(10):
    if p == A[i]:
        ans = 'Yes'
        break
print(ans)
