a = int(input())
print(str(int((a / 3600) % 24)) + ':' + str(int(((a / 60) % 60) / 10)) + str(int(((a / 60 % 60) % 10))) + ':' + str(
    int((a % 60) / 10)) + str(int((a % 60)) % 10))
