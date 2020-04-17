a, b, n = int(input()), int(input()), int(input())
if n == 1:
    print('>A')
    print('A>B')
    print('>A')
    print('A>B')
elif n == 2:
    print('>B')
    print('B>A')
elif n == 3:
    print('>A')
    print('A>B')
    print('>A')
    print('A>B')
    print('B>')
    print('A>B')
    print('>A')
    print('A>B')
elif n == 4:
    print('>A')
    print('A>B')
    print('')
elif n == 5:
    print('>B')
elif n >= 6:
    print('Impossible')
# 3 5