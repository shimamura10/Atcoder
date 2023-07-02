n = int(input())
a,b,c,d = 0,0,0,0
for i in range(n):
    s = input()
    if s == 'AC':
        a += 1
    elif s == 'WA':
        b += 1
    elif s == 'TLE':
        c += 1
    elif s == 'RE':
        d += 1
print('AC x '+str(a))
print('WA x '+str(b))
print('TLE x '+str(c))
print('RE x '+str(d))