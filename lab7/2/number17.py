k = int(input())
# if k % 3 == 0 or k % 5 == 0 or (k - (k // 5) * 5) % 3 == 0 or (k - (k // 3) * 3) % 5 == 0:
#     print('YES')
# else:
#     print('NO')
if k == 0 or k == 1 or k == 2 or k == 4 or k == 7:
    print('NO')
else:
    print('YES')
