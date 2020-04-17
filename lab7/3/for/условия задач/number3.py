import math

a, b = int(input()), int(input())
for i in range(a,b+1):
    if int(math.sqrt(i)) == math.sqrt(i):
        print(i)
