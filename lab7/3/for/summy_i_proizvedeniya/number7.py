n = int(input())
res = 1
for i in range(1, n+1):
    res += ((-1)**i) / (2*i + 1)
print(4 * res)