L = int(input())
L -= 12
import math
ans = math.factorial(L + 11)//math.factorial(L)//math.factorial(11)
print(ans)