from random import randint
def list_rand(N,m,M):
    return [randint(m,M) for _ in range(N)]
def list2_rand(H,W,m,M):
    return [[randint(m,M) for _ in range(W)] for _ in range(H)]
abc = 'abcdefghijklmnopqrstuvwxyz'
def str_rand(N):
    ret = ''
    for _ in range(N):
        ret += abc[randint(1,26)]
    return ret

def random_generate():
    # 入力をランダムに生成
    H = randint(1,10)
    N = randint(1,10)    #randint(a,b) a <= i <= b となる整数i
    A = [randint(1,10) for _ in range(N)]
    B = [randint(1,10) for _ in range(N)]
    return H,N,A,B

def solve(h,n,A,B):
    # 自分の解を書く
    # h,n=map(int,input().split())
    # h,n,A,B = random_generate()
    dp=[[10**9]*(h+1) for _ in range(n+1)]
    done=[[False]*(h+1) for _ in range(n+1)]
    for i in range(n+1):
        done[i][0]=True
        dp[i][0]=0
    over=10**18
    for i in range(1,n+1):
        # a,b=map(int,input().split())
        a = A[i-1]
        b = B[i-1]
        for j in range(h+1):
            if j>=a:
                if dp[i][j]>dp[i][j-a]+b and done[i][j-a]:
                    dp[i][j]=dp[i][j-a]+b
                    done[i][j]=True
                if dp[i][j]>dp[i-1][j-a]+b and done[i-1][j-a]:
                    dp[i][j]=dp[i-1][j-a]+b
                    done[i][j]=True
            if dp[i][j]>dp[i-1][j] and done[i-1][j]:
                dp[i][j]=dp[i-1][j]
                done[i][j]=True
            if done[i][j] and j+a>=h:
                over=min(over,dp[i][j]+b)

    return min(dp[-1][-1],over)

def solve_Jury(H,N,A,B):
    # 遅いが正しいプログラムを書く
    dp = [10**9]*(H+1)
    dp[0] = 0
    for i in range(N):
        a = A[i]
        b = B[i]
        for j in range(1,H+1):
            dp[j] = min(dp[j],dp[max(0,j-a)]+b)
    # print(dp[H])
    return dp[H]

cnt = 0
for i in range(1000):
    H,N,A,B = random_generate()
    ans1 = solve(H,N,A,B)
    ans2 = solve_Jury(H,N,A,B)
    if ans1 != ans2:
        print('No.'+str(i))
        print(H)
        print(N)
        print(A)
        print(B)
        print(ans1,ans2)
        cnt += 1
    if cnt >= 5:
        break