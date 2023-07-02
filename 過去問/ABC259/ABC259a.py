N,M,X,T,D = map(int,input().split())
if M <= X:
    print(T-(X-M)*D)
else:
    print(T)