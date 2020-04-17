h = int(input())
a = int(input())
b = int(input())
c = 0
cnt = 0
value = True
while value:
    c += a
    if c >= h:
        cnt += 1
        value = False
    else:
        c -= b
        cnt += 1
print(cnt)
