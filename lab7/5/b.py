def my_power(a,n):
	d = 1
	for x in range(1,n+1):
		d = d * a
	print(d)

num = input()
snum = num.split()
my_power(float(snum[0]),int(snum[1]))