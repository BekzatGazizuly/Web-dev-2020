counter = 0
temp = -1000
while True:
    a = int(input())
    if a == 0:
        print(counter - 1)
        break
    if a > temp:
        counter += 1
    temp = a
