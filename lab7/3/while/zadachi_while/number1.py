import math

n = int(input())
i = 1
condition = True
while condition:
    if i <= n:
        if int(math.sqrt(i)) == math.sqrt(i):
            print(i)
        i += 1
    else:
        condition = False
