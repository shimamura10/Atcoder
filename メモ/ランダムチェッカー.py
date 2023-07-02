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
    N = randint(1,10)    #randint(a,b) a <= i <= b となる整数i
    A = [randint(1,10) for _ in range(N)]
    B = [randint(1,10) for _ in range(N)]
    return N,A,B

def solve(N,A,B):
    # 自分の解を書く
    return 

def solve_Jury(N,A,B):
    # 遅いが正しいプログラムを書く
    return 

cnt = 0
for i in range(1000):
    N,A,B = random_generate()
    ans1 = solve(N,A,B)
    ans2 = solve_Jury(N,A,B)
    if ans1 != ans2:
        print('No.'+str(i))
        print(N)
        print(A)
        print(B)
        print(ans1,ans2)
        cnt += 1
    if cnt >= 5:
        break
