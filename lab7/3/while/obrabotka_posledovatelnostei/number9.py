counter = 0
maximum = -1000
while True:
    a = int(input())
    if a == 0:
        print(counter)
        break
    if a > maximum:
        maximum = a
        counter = 0
    if a == maximum:
        counter += 1
