x, y = int(input()), int(input())
counter = 0
while x < y:
    x += 0.1 * x
    counter += 1
else:
    print(counter+1)
