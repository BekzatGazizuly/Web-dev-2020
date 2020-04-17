a = int(input())
b = int(input())
if b % a == 0:
    print(0)
else:
    print(a - b % a)
