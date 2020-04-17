max = -1000
while True:
    a = int(input())
    if a == 0:
        print(max)
        break
    if a > max:
        max = a
