n = int(input())
if n % 100 == (11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19) or (
        n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 or n % 10 == 0):
    print(n, 'bochek')
elif n % 10 == 1:
    print(n, 'bochka')
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    print(n, 'bochki')
