n = int(input())
res = 2
if n == 0:
    res = 1
else:
    for i in range(1, n):
        res *= 2
print(res)
