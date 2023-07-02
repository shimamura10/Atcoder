S = input()
ans = ''
for s in S:
    ans += chr(ord(s)-ord('a')+ord('A'))
print(ans)