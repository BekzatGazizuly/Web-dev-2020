import math

# a, b, c = int(input()), int(input()), int(input())
# d = b ** 2 - 4 * a * c
# if d > 0:
#     x1 = int((-b + math.sqrt(d)) / (2 * a))
#     x2 = int((-b - math.sqrt(d)) / (2 * a))
#     print(x1, x2)
# elif d == 0:
#     print(int(-b / 2 * a))


a = float(input())
b = float(input())
c = float(input())

r = b ** 2 - 4 * a * c

if r > 0:
    x1 = (((-b) + math.sqrt(r)) / (2 * a))
    x2 = (((-b) - math.sqrt(r)) / (2 * a))
    print(int(x1), int(x1))
elif r == 0:
    x = (-b) / 2 * a
    print(int(x))
else:
    num_roots = 0
