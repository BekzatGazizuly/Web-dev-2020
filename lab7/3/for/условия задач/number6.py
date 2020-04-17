# a = int(input())
# cnt = 0
# for i in range(1, a + 1):
#     if a % i == 0:
#         cnt += 1
# print(cnt)
x = int(input())
d = 2  # 1 и само число
for i in range(2, int(x / 2) + 1):  #
    if x % i == 0:
        d += 1

print(d)