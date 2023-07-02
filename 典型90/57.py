N,M = map(int,input().split())
gyouretu = []
for _ in range(N):
    T = int(input())
    A = list(map(int,input().split()))
    tmp = [0]*M
    for a in A:
        tmp[a-1] = 1
    gyouretu.append(tmp)
S = list(map(int,input().split()))
cnt = 0
for i in range(M):
    init = -1
    for j in range(cnt,N):
        if gyouretu[j][i]:
            if init == -1:
                init = j
            else:
                for k in range(M):
                    gyouretu[j][k] ^= gyouretu[init][k]
    if init >= 0:
        # gyouretu = gyouretu[:cnt] + [gyouretu[init]] + gyouretu[cnt:init] + gyouretu[init+1:]
        gyouretu[cnt], gyouretu[init] = gyouretu[init], gyouretu[cnt]
        cnt += 1
        if cnt == N:
            break
now = [0]*M
seen = 0
for i,s in enumerate(S):
    if now[i] != s:
        if seen < N and gyouretu[seen][i]:
            for j,a in enumerate(gyouretu[seen]):
                if a:
                    now[j] = 1 - now[j]
            seen += 1
        else:
            print(0)
            exit()
    else:
        if seen < N and gyouretu[seen][i]:
            seen += 1
print(pow(2,N-seen,998244353))