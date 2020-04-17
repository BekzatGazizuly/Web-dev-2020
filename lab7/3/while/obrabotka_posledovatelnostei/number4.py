counter = 0
while True:
    a = int(input())
    if a == 0:
        print(counter)
        break
    if a % 2 == 0:
        counter += 1