# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if (abs((x2 - x1) or (y2 - y1)) == 1) or ((abs(x1 - x2) == 1) and y1 == y2) or ((abs(y1 - y2) == 1) and x1 == x2):
#     print('YES')
# else:
#     print('NO')

import math

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if x1 == x2 and abs(y1 - y2) == 1:
    print('YES')
elif abs(x1 - x2) == 1 and abs(y1 - y2) == 1:
    print('YES')
elif abs(x1 - x2) == 1 and y1 == y2:
    print('YES')

else:
    print('NO')
