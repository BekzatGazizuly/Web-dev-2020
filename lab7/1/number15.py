a = int(input())
b = int(input())
n = int(input())
a *= n
b *= n
if b > 100:
    a += b // 100
    b -= (b // 100)*100
print(a, b)
