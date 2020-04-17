a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a == 0 and b == 0:
    print('INF')
else:
    if a == 0 or b % a != 0 or c * (-b / a) + d == 0:
        print('NO')
    else:
        print(int(-b / a))
