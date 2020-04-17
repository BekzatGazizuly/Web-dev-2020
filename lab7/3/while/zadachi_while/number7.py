x, p, y = int(input()), int(input()), int(input())
counter = 0
while x < y:
    x += x * p * 0.01
    x = int(x)
    counter += 1
else:
    print(counter)
