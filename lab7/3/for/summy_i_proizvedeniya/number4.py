n, k = int(input()), int(input())
res1 = 1
res2 = 1
res3 = 1
for i in range(1, n + 1):
    res1 *= i
for i in range(1, k + 1):
    res2 *= i
for i in range(1, n - k + 1):
    res3 *= i
print(int(res1 / (res2 * res3)))
