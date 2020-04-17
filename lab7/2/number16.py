a, b, c, d = int(input()), int(input()), int(input()), int(input())
a *= 100
c *= 100
x = a + b
y = c + d
z = y - x
print(z // 100, z % 100)
