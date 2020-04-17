# 3
# 3
# 6
# k, m, n = int(input()), int(input()), int(input())
# if n % k == 0:
#     raz = int(n / k)
# else:
#     raz = int(n / k) + 1
# temp = 0
# if n <= k:
#     print(2 * m)
# else:
#     for i in range(0, raz):
#         temp += 2 * m
#     print(temp)

k = int(input())
m = int(input())
n = int(input())
if n <= k:
    t = 2 * m
elif n * 2 % k == 0:
    t = m * (n * 2 // k)
else:
    t = m * (1 + (n * 2 // k))
print(t)
