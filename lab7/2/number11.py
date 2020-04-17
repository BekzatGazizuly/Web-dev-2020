# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if abs(x2 - x1) == 2:
#     if abs(y2 - y1) == 1:
#         print('YES')
#     else:
#         print('NO')
# elif abs(x2 - x1) == 1:
#     if abs(y2 - y1) == 2:
#         print('YES')
#     else:
#         print('NO')
# elif x1 == x2 and y1 == y2:
#     print('NO')

# if x1 == x1 and y1 != y2:
#     print('YES')
# else:
#     print('NO')
import math

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())  # 5,4
if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:  # 1: 3,5 and 3,3     #4: 7,5 and 7,3
    print('YES')
elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:  # 2: 4,6 and 4,2     #3: 6,6 and 6,2
    print('YES')
else:
    print('NO')
