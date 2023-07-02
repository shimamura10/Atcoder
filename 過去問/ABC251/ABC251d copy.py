W = int(input())
ans = [i+1 for i in range(100)] + [(i+1)*100 for i in range(100)] + [(i+1)*10000 for i in range(100)]
print(len(ans))
print(*ans)