from math import acos, degrees

a, b, c = int(input()), int(input()), int(input())
# if a ** 2 + b ** 2 == c ** 2 or c ** 2 + b ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
#     print('right')
# elif degrees(acos(a ** 2 + b ** 2 - c ** 2) / 2 * a * b) or degrees(
#         acos(b ** 2 + c ** 2 - a ** 2) / 2 * b * c) or degrees(acos(a ** 2 + c ** 2 - b ** 2) / 2 * a * c) < 90:
#     print('acute')
# elif degrees(acos(a ** 2 + b ** 2 - c ** 2) / 2 * a * b) or degrees(
#         acos(b ** 2 + c ** 2 - a ** 2) / 2 * b * c) or degrees(acos(a ** 2 + c ** 2 - b ** 2) / 2 * a * c) > 90:
#     print('obtuse')


# x = ((a ** 2) - (b ** 2) - (c ** 2))/(- 2 * b * c)
# y = ((b ** 2) - (a ** 2) - (c ** 2))/(- 2 * a * c)
# z = ((c ** 2) - (a ** 2) - (b ** 2))/(- 2 * b * a)
# if x or y or z == 0:
#     print("right")
# elif x and y and z > 0:
#     print("acute")
# elif x or y or z < 0:
#     print("obtuse")

# if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (c*c + b*b == a*a):
#     print("right")
# elif (a*a + b*b < c*c) or (a*a + c*c < b*b) or (c*c + b*b < a*a):
#     print("obtuse")
# else:
#     print("acute")
if a < b + c and b < a + c and c < a + b:
    if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2):
        print('right')
    elif (a ** 2 > b ** 2 + c ** 2) or (b ** 2 > a ** 2 + c ** 2) or (c ** 2 > a ** 2 + b ** 2):
        print('obtuse')
    else:
        print('acute')
else:
    print('impossible')
