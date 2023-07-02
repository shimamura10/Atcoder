s = input()
if s[-1] == 's':
    s += 'es'
    print(''.join(s))
else:
    s += 's'
    print(''.join(s))