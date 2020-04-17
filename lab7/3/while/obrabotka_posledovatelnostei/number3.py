avg = 0
counter = 0
sum = 0
while True:
    a = int(input())
    counter += 1
    if a == 0:
        print(avg)
        break
    else:
        sum += a
        avg = sum / counter
