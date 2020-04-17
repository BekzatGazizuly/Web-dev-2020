a = int(input())
b = int(input())
x = -b / a
if a == 0 and b == 0:
    print('INF')
else:
    if a == 0 or b % a != 0:
        print('NO')
    else:
        print(int(-b / a))
