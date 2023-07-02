S = input()
a = ord('a')
for i,s in enumerate(S):
    if ord(s) < a:
        print(i+1)
        exit()