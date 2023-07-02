s = input()
S = [int(i) for i in s]
for i in range(10):
    if i not in S:
        print(i)