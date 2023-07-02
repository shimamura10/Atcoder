N = int(input())
C = input()
nr = 0
nw = 0
for c in C:
    if c == 'W':
        nw += 1
nr = N - nw
nrc = 0
nwc = 0
for i in range(nr):
    if C[i] == 'R':
        nrc += 1
for i in range(nw):
    if C[-(i+1)] == 'W':
        nwc += 1
print(max(nr-nrc,nw-nwc))