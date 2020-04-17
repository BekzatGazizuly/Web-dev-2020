sum = 0
temporary = 0
while True:
    a = int(input())
    if a == 0 and temporary == 0:
        print(sum)
        break
    temporary = a
    sum += a
# w = 0
# zeros = 0
# while True:
#     a = int(input())
#     w += a
#     zeroes = zeroes + 1 if not a else 0
#     if zeroes == 2:
#         break
#
# print(w)
