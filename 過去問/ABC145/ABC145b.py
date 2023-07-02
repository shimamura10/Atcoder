N = int(input())
S = input()
if N%2:
    print('No')
else:
    for i in range(N//2):
        if S[i] != S[i+N//2]:
            print('No')
            exit()
    print('Yes')