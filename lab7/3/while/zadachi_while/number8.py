n = int(input())
f_cur_2 = 0
f_cur_1 = 1
f_cur = 1
counter = 2
while counter < n:
    f_cur_2 = f_cur_1
    f_cur_1 = f_cur
    f_cur = f_cur_1 + f_cur_2
    counter += 1
else:
    print(f_cur)
#  0 1 1 2 3 5 8