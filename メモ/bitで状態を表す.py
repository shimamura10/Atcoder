seen = [[False]*W for _ in range(H)]
bit = 0

seen[i][j] = True
bit |= 1 << i*W + j

if seen [i][j] == True:
if bit >> i*W + j &1:
