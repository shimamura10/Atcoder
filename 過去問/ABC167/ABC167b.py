A,B,C,K = map(int,input().split())
ans = 0
if K <= A:
    ans += K
    K = 0
else:
    ans += A
    K -= A
if K <= B:
    K = 0
else:
    K -= B
ans -= min(K,C)
print(ans)
