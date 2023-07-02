from random import randint


N = input()
N = [int(i) for i in N]
N = N[::-1]
N.append(0)

for i in range(len(N)-1):
    if N[i] > 5:
        N[i] = 10 - N[i]
        N[i+1] += 1
    elif N[i] == 5:
        if N[i+1] >= 5:
            N[i+1] += 1
print(sum(N))

# ans = 0
# up = False
# for i,n in enumerate(N):
#     # n = int(N[i])
#     if n == 9 and up:
#         continue
#     if n + up > 5:
#         ans += 10 - n - up
#         up = True
#     elif n + up == 5:
#         if N[i+1] >= 5:
#             ans += 10 - n - up
#             up = True
#         else:
#             ans == n + up
#             up = False
#     else:
#         ans += n + up
#         up = False
#     # ans += min(n,11-n)
# print(ans+up)

# def solve():
#     N = [randint(0,9) for _ in range(3)]
#     ans = 0
#     up = False
#     for i in reversed(range(len(N))):
#         n = N[i]
#         if n == 9 and up:
#             continue
#         if n + up > 5:
#             ans += 10 - n - up
#             up = True
#         else:
#             ans += n + up
#             up = False
#     print(N,ans)
# for _ in range(10):
#     solve()
# from random import randint
# def list_rand(N,m,M):
#     return [randint(m,M) for _ in range(N)]
# def list2_rand(H,W,m,M):
#     return [[randint(m,M) for _ in range(W)] for _ in range(H)]
# abc = 'abcdefghijklmnopqrstuvwxyz'
# def str_rand(N):
#     ret = ''
#     for _ in range(N):
#         ret += abc[randint(1,26)]
#     return ret

# def random_generate():
#     # 入力をランダムに生成
#     N = randint(1,10)    #randint(a,b) a <= i <= b となる整数i
#     A = [randint(1,10) for _ in range(N)]
#     B = [randint(1,10) for _ in range(N)]
#     return N,A,B

# def solve(N,A,B):
#         # 自分の解を書く
#     ans = 0
#     up = False
#     for i in reversed(range(len(N))):
#         n = int(N[i])
#         if n == 9 and up:
#             continue
#         if n + up > 5:
#             ans += 10 - n - up
#             up = True
#         else:
#             ans += n + up
#             up = False
#         # ans += min(n,11-n)
#     return ans+up



# def solve_Jury(N,A,B):
#     # 遅いが正しいプログラムを書く
#     ans = 10**5
#     for i in range(len(N)):
#         for j in range(10)
#     return 

# cnt = 0
# for i in range(1000):
#     N,A,B = random_generate()
#     ans1 = solve(N,A,B)
#     ans2 = solve_Jury(N,A,B)
#     if ans1 != ans2:
#         print('No.'+str(i))
#         print(N)
#         print(A)
#         print(B)
#         print(ans1,ans2)
#         cnt += 1
#     if cnt >= 5:
#         break

# N =int(input())
# A = list(map(int,input().split()))
# ans = 0
# ok = True
# while True:
#     for i in range(N):
#         if A[i] % 2 == 0:
#             A[i] //= 2
#         else:
#             ok = False
#             break
#     if ok == False:
#         break
#     ans += 1