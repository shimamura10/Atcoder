X,A,D,N = map(int,input().split())
if D == 0:
    print(abs(X-A))
    exit()
n = (X-A)//D
n = min(n,N-2)
n = max(n,0)
a = A + n*D
b = A + (n+1)*D
ans = min(abs(X-a),abs(X-b))
print(ans)