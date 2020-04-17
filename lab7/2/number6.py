a = int(input())
b = int(input())
c = int(input())
temp = 0
max = 0
if a > b:
    temp = a
elif a < b:
    temp = b
else:
    temp = a

if temp > c:
    max = temp
elif temp < c:
    max = c
else:
    max = temp
print(max)
