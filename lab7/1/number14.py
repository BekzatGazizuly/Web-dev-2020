'''
 9:00
 1- 9:45 (+5)
 50
 2- 10:35 (+15) 1+50
 60
 3- 11:35 (+5)  1+110
 50
 4- 12:25 (+15) 1+160
 60
 5- 13:25 (+5) 1+220
 50
 6- 14:15 (+15) 1+270
 60
 7- 15:15 (+5) 1+330
 50
 8- 16:05 (+15) 1+380
 60
 9- 17:05 (+5) 1+420
 50
10- 17:55 1+470

1- 45| == 0
2- 45 45| 5 == 5
3- 45 45 45| 5 15 == 20
4- 45 45 45 45| 5 15 5 == 25
5- 45 45 45 45 45| 5 15 5 15 == 40
6- 45 45 45 45 45 45| 5 15 5 15 5 == 45

1- 0
2- 45 5
3- 45 45 5 15
4- 45 45 45 5 15 5
5- 45 45 45 45 5 15 5 15



'''
# a = int(input())
# # print(int(9 + (((a * 45) + a / 2 * 5 + (a - 1) / 2 * 15) / 60)), int(((a * 45) + a / 2 * 5 + (a - 1) / 2 * 15) % 60))
# if a == 1:
#     print(9, 45)
# elif a == 2:
#     print(10, 35)
# elif a == 3:
#     print(11, 35)
# elif a == 4:
#     print(12, 25)
# elif a == 5:
#     print(13, 25)
# elif a == 6:
#     print(14, 15)
# elif a == 7:
#     print(15, 15)
# elif a == 8:
#     print(str(16) + ' 05')
# elif a == 9:
#     print(str(17) + ' 05')
# elif a == 10:
#     print(17, 55)

a = int(input())
a = a * 45 + (a // 2) * 5 + ((a + 1) // 2 - 1) * 15
print(a // 60 + 9, a % 60)
