S = input()
if S[0] == '1':
    print("No")
    exit()
pin = []
num = [[7], [4], [8,2], [5], [9,3], [6], [10]]
for i in range(7):
    for n in num[i]:
        n -= 1
        if S[n] == '1':
            pin.append(i)
for i in range(len(pin)-1):
    if pin[i+1] - pin[i] > 1:
        print("Yes")
        exit()
print("No")
