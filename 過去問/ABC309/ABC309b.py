N = int(input())
A = [input() for _ in range(N)]
B = [a for a in A]
B[0] = A[1][0] + A[0][:N-1]
B[N-1] = A[N-1][1:] + A[N-2][N-1]
for i in range(1,N-1):
  B[i] = A[i+1][0] + B[i][1:N-1] + A[i-1][N-1]
for b in B:
  print(b)