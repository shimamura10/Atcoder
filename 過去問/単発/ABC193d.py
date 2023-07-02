K = int(input())
S = input()
T = input()
seenS = [0]*10
seenT = [0]*10
for i in range(4):
    seenS[int(S[i])] += 1
    seenT[int(T[i])] += 1
ans = 0
for s in range(1,10):
    for t in range(1,10):
        seenS[s] += 1
        tmp = (K-seenS[s]-seenT[s]+1)/(9*K-8)
        seenT[t] += 1
        tmp *= (K-seenT[t]-seenS[t]+1)/(9*K-9)
        ps = 0
        pt = 0
        if seenS[s] + seenT[s] > K or seenT[t] + seenS[t] > K:
            seenS[s] -= 1
            seenT[t] -= 1
            continue
        for i in range(10):
            ps += i*10**seenS[i]
            pt += i*10**seenT[i]
        if ps > pt:
            ans += tmp
        seenS[s] -= 1
        seenT[t] -= 1
print(ans)
