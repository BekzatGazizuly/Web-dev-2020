n = int(input())
f_cur_2 = 0
f_cur_1 = 1
f_cur = 1
counter = 2
if n == 0:
    print(0)
elif n == 1:
    print(1)
while counter < n:
    f_cur_2 = f_cur_1
    f_cur_1 = f_cur
    f_cur = f_cur_1 + f_cur_2
    counter += 1
    if f_cur < n:
        continue
    elif f_cur == n:
        print(counter)
        break
    else:
        print(-1)
        break

#  0 1 1 2 3 5 8