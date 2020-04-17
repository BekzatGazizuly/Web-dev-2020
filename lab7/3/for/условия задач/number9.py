positive = 0
negative = 0
zeros = 0
#n = int(input())
for i in range(int(input())):
    a = int(input())
    if a > 0:
        positive += 1
    elif a < 0:
        negative += 1
    elif a == 0:
        zeros += 1
print(zeros, positive, negative)
