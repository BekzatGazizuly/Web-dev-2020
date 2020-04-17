a, n = int(input()), int(input())
res = 0
for i in range(0, n+1):
    res += a**i
print(res)
