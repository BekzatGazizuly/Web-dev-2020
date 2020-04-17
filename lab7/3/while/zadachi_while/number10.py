a, b = int(input()), int(input())
while a != b:
    if a / 2 > b:
        if a % 2 == 0:
            a /= 2
            print(':2')
            if a == b:
                break
        else:
            a -= 1
            print('-1')
            if a == b:
                break
    else:
        a -= 1
        print('-1')
        if a == b:
            break
