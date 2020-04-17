def my_xor(x,y):
	if x == y:
		print(0)
	else:
		print(1)

num = [int(i) for i in input().split()]
my_xor(num[0],num[1])