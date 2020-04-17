import math

n = int(input())
res = 1
for i in range(1, n+1):
    res += 1/math.factorial(i)
# res = float('{:.5f}'.format(res))
print(int(res))
